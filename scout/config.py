"""Paths, port, model and the `.env` loader. Nothing here prints a secret."""
import os
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PORT = int(os.environ.get('SCOUT_PORT', '8780'))
MODEL = 'claude-opus-5'
MAX_TOOL_ROUNDS = 8


def load_env(path=None):
    """Read KEY=VALUE lines from `.env` into os.environ without overriding what is set."""
    p = Path(path) if path else ROOT / '.env'
    if not p.exists():
        return
    for line in p.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k, _, v = line.partition('=')
        k, v = k.strip(), v.strip().strip('"').strip("'")
        if k and k not in os.environ:
            os.environ[k] = v


load_env()

DATA = Path(os.environ.get('SCOUT_DATA_DIR') or ROOT / 'data')
RUN = DATA / 'run'
BRIEFS = RUN / 'briefs'
FIELDS = RUN / 'fields'
CHATS = DATA / 'chats'
WEB_DIST = ROOT / 'web' / 'dist'
HACKATHONS = DATA / 'hackathons.jsonl'
HACKATHONS_ALL = DATA / 'hackathons_all.jsonl'
IDEAS_DB = DATA / 'ideas.db'
FACETS = DATA / 'facets.jsonl'
VAULT = ROOT / 'vault'
TAXONOMY = ROOT / 'hub' / 'taxonomy.json'


def has_api_key():
    return bool(os.environ.get('ANTHROPIC_API_KEY'))


def mode():
    return 'claude' if has_api_key() else 'local'


def census_date():
    """The census is dated by the index file, not by the clock."""
    if HACKATHONS.exists():
        return datetime.fromtimestamp(HACKATHONS.stat().st_mtime).date().isoformat()
    return None


def today():
    """Today, overridable for tests (SCOUT_TODAY=YYYY-MM-DD)."""
    t = os.environ.get('SCOUT_TODAY')
    return date.fromisoformat(t) if t else date.today()
