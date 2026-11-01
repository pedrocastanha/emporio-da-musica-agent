from __future__ import annotations

import sqlite3
from pathlib import Path

from .config import settings

TICKETS_SCHEMA = """
CREATE TABLE IF NOT EXISTS handoff_tickets (
    ticket_id        TEXT PRIMARY KEY,
    created_at       TEXT NOT NULL,
    reason           TEXT NOT NULL,
    summary          TEXT NOT NULL,
    customer_contact TEXT,
    order_id         TEXT,
    status           TEXT NOT NULL DEFAULT 'open'
)
"""


def connect(path: Path | None = None) -> sqlite3.Connection:
    path = Path(path or settings.db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path), check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute(TICKETS_SCHEMA)
    conn.commit()
    return conn
