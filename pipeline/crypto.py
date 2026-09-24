"""Family-password encryption for the published site and for the data committed to Git.

- The site: each page is AES-GCM encrypted; the browser derives the same key from the
  password (PBKDF2-SHA256) and decrypts it (see assets/lock.js).
- The repo: cache/ is gitignored; `lock` writes an encrypted mirror to vault/ and `unlock`
  restores it. Encryption there is deterministic per file, so unchanged files produce
  identical ciphertext and Git only sees real changes.
"""

import base64
import hashlib
import hmac
import os
from functools import cache
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from .config import CACHE_DIR, ROOT, VAULT_DIR

PBKDF2_ITERATIONS = 600_000
SITE_SALT = b"recetario/site/v1"
DATA_SALT = b"recetario/data/v1"
ENCRYPTED_SUFFIX = ".enc"


def password() -> str:
    from dotenv import load_dotenv

    load_dotenv(ROOT / ".env")
    value = os.environ.get("RECETARIO_PASSWORD", "")
    if not value:
        raise SystemExit(
            "Falta RECETARIO_PASSWORD. Añádela a .env (local) o como secreto del repositorio (GitHub Actions)."
        )
    return value


@cache
def derive_key(salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", password().encode("utf-8"), salt, PBKDF2_ITERATIONS, dklen=32)


def encrypt_page(plaintext: str) -> str:
    """Random nonce; returns base64(nonce + ciphertext) for embedding in HTML."""
    nonce = os.urandom(12)
    ciphertext = AESGCM(derive_key(SITE_SALT)).encrypt(nonce, plaintext.encode("utf-8"), None)
    return base64.b64encode(nonce + ciphertext).decode("ascii")


def opaque_id(name: str) -> str:
    """Stable, unguessable URL segment for a page, so folder names don't reveal recipe titles."""
    return hmac.new(derive_key(SITE_SALT), name.encode("utf-8"), hashlib.sha256).hexdigest()[:12]


def _seal(relpath: str, data: bytes) -> bytes:
    key = derive_key(DATA_SALT)
    nonce = hmac.new(key, relpath.encode() + b"\0" + data, hashlib.sha256).digest()[:12]
    return nonce + AESGCM(key).encrypt(nonce, data, relpath.encode())


def _open(relpath: str, blob: bytes) -> bytes:
    return AESGCM(derive_key(DATA_SALT)).decrypt(blob[:12], blob[12:], relpath.encode())


def _vault_path(relpath: str) -> Path:
    return VAULT_DIR / (relpath + ENCRYPTED_SUFFIX)


def lock() -> None:
    """Encrypt cache/ into vault/ (commit vault/, never cache/)."""
    live, changed = set(), 0
    for path in sorted(CACHE_DIR.rglob("*")):
        if not path.is_file() or path.suffix == ".tmp":
            continue
        relpath = path.relative_to(CACHE_DIR).as_posix()
        live.add(relpath)
        target = _vault_path(relpath)
        blob = _seal(relpath, path.read_bytes())
        if not target.exists() or target.read_bytes() != blob:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(blob)
            changed += 1
    removed = 0
    for target in VAULT_DIR.rglob(f"*{ENCRYPTED_SUFFIX}"):
        if target.relative_to(VAULT_DIR).as_posix()[: -len(ENCRYPTED_SUFFIX)] not in live:
            target.unlink()
            removed += 1
    print(f"vault/: {changed} archivos cifrados, {removed} eliminados, {len(live)} en total")


def unlock(force: bool = False) -> None:
    """Restore cache/ from vault/ (after cloning, or in GitHub Actions)."""
    restored = skipped = 0
    for target in sorted(VAULT_DIR.rglob(f"*{ENCRYPTED_SUFFIX}")):
        relpath = target.relative_to(VAULT_DIR).as_posix()[: -len(ENCRYPTED_SUFFIX)]
        path = CACHE_DIR / relpath
        if path.exists() and not force:
            skipped += 1
            continue
        try:
            data = _open(relpath, target.read_bytes())
        except Exception:
            raise SystemExit(f"No se pudo descifrar {relpath}: ¿contraseña incorrecta?") from None
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        restored += 1
    print(f"cache/: {restored} archivos restaurados, {skipped} ya existían (usa --force para sobrescribir)")
