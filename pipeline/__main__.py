"""python -m pipeline {audit|extract|cluster|consolidate|verify|scans|render|serve|all|lock|unlock} [--pages 1-5] [--force]"""

import argparse
import sys

from . import audit, cluster, consolidate, crypto, extract, render, scans, verify


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(prog="python -m pipeline")
    parser.add_argument("step", choices=["audit", "extract", "cluster", "consolidate", "verify", "scans", "render", "serve", "all", "lock", "unlock"])
    parser.add_argument("--pages", help="extract only these pages, e.g. 1-5,9,100")
    parser.add_argument("--force", action="store_true", help="redo cached pages/recipes/scans; with unlock, overwrite cache/")
    args = parser.parse_args()

    if args.step == "unlock":
        crypto.unlock(args.force)
    if args.step == "audit":
        audit.run()
    if args.step in ("extract", "all"):
        extract.run(args.pages, args.force)
    if args.step in ("cluster", "all"):
        cluster.run()
    if args.step in ("consolidate", "all"):
        consolidate.run(args.force)
    failing = verify.run() if args.step in ("verify", "all") else []
    # Keep the committed, encrypted copy in step with anything that just changed cache/.
    if args.step in ("audit", "extract", "cluster", "consolidate", "verify", "all", "lock"):
        crypto.lock()
    if args.step in ("scans", "all"):
        scans.run(args.force)
    if args.step in ("render", "all"):
        render.run()
    if args.step == "serve":
        render.serve()
    if args.step == "verify" and failing:
        sys.exit(1)


if __name__ == "__main__":
    main()
