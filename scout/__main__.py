"""python3 -m scout  → serve web/dist + /api on http://127.0.0.1:8780"""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scout import config                                             # noqa: E402
from scout.server import serve                                       # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--host', default='127.0.0.1')
    ap.add_argument('--port', type=int, default=config.PORT)
    ap.add_argument('--quiet', action='store_true', help='no per-request log lines')
    a = ap.parse_args()
    serve(a.host, a.port)


if __name__ == '__main__':
    main()
