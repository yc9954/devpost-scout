"""Scout: the devpost-scout toolkit as one product — a chat agent plus a dashboard."""
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:                      # hub/, discover/, lib/ import as packages
    sys.path.insert(0, str(_ROOT))
