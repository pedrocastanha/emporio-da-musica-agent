from __future__ import annotations

import os
from datetime import datetime
from zoneinfo import ZoneInfo

from .config import STORE_TZ

TZ = ZoneInfo(STORE_TZ)


def now() -> datetime:
    override = os.getenv("EMPORIO_NOW")
    if override:
        dt = datetime.fromisoformat(override)
        return dt if dt.tzinfo else dt.replace(tzinfo=TZ)
    return datetime.now(TZ)
