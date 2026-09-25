# recetario
From binder pages to web: an automated pipeline for a recipe collection

Scans in `pictures/` (not committed) → structured JSON → consolidated recipes → a static cookbook site on GitHub Pages.

## Setup

```sh
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt   # macOS/Linux: .venv/bin/pip
cp .env.example .env                            # then add ANTHROPIC_API_KEY and RECETARIO_PASSWORD
```

## Pipeline

```sh
python -m pipeline audit                  # 1. gaps, duplicates, blurry scans (no API calls)
python -m pipeline extract --pages 9-12   # 2. vision pass on a few pages first; check cache/pages/
python -m pipeline extract                # 2. all remaining pages (cached pages are skipped)
python -m pipeline cluster                # 3. group continuations and duplicates (no API calls)
python -m pipeline consolidate            # 4. merge each group into one recipe + category/tags
python -m pipeline verify                 # 5. check every recipe against its pages (no API calls)
python -m pipeline render                 # 6. build the site into site/
python -m pipeline serve                  # preview at http://localhost:8000 (also reachable from a phone on the same Wi-Fi)
```

`python -m pipeline all` runs steps 2–6. Things to check by hand go to `cache/review.md`. You fix them in `data/overrides.yaml` (merge/split recipes, drop pages, correct a category), then re-run `cluster`, `consolidate` and `render`. Only recipes whose source pages changed call the API again.

`verify` catches consolidated recipes that drifted from the scans. It flags ingredients, quantities, oven temperatures, times and servings that aren't on the page, and page ingredients the recipe dropped (❌). It also flags steps and notes built mostly from words the page doesn't use (⚠️, often just rewording). It exits with an error while any ❌ remain. Fix the recipe in `cache/recipes/` or re-consolidate it. If the scan shows it's right, add its id to `verified:` in `data/overrides.yaml`.

All model calls live in `pipeline/llm.py`. Models are set in `pipeline/config.py`, and so are the categories and tags. The site's HTML is generated in `pipeline/render.py`, and the look comes from `pipeline/assets/` (`style.css`, `app.js`).

## Privacy

The recipes are for the family only. One password, `RECETARIO_PASSWORD`, protects both copies:

- **In Git:** `cache/` (plain text) is gitignored. Every pipeline step re-encrypts it into `vault/`, which is what gets committed. After cloning, run `python -m pipeline unlock` to restore `cache/`. You can also encrypt by hand with `python -m pipeline lock`.
- **On the website:** every page, including its title and URL, is encrypted (AES-GCM, with the key derived from the password using PBKDF2). Visitors see a password screen. Each device can remember the password, and "Cerrar sesión" makes it forget.

Use a long passphrase (4–5 random words). The encrypted files are public, so a short password could be guessed offline. To change the password, update `.env` and the GitHub secret, then run `python -m pipeline lock` and push. Everyone then has to enter the new password.

## Deploy

Pushing to `main` runs `.github/workflows/deploy.yml`. It decrypts `vault/`, builds the site and publishes it. No API key or scans are needed there. One-time setup on GitHub:

1. Settings → Secrets and variables → Actions → New repository secret: `RECETARIO_PASSWORD`.
2. Settings → Pages → Source: **GitHub Actions**.
