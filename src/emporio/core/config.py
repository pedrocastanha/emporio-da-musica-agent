"""Central configuration: paths and environment-driven settings, loaded from .env."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[3]
load_dotenv(ROOT / ".env")

RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
VAR_DIR = ROOT / "var"

STORE_TZ = "America/Campo_Grande"


def _env(name: str, default: str | None = None) -> str | None:
    value = os.getenv(name)
    return value if value else default


@dataclass(frozen=True)
class Settings:
    openai_api_key: str | None = field(default_factory=lambda: _env("OPENAI_API_KEY"), repr=False)
    chat_model: str = field(default_factory=lambda: _env("EMPORIO_CHAT_MODEL", "gpt-4.1-mini"))
    embedding_model: str = field(
        default_factory=lambda: _env("EMPORIO_EMBEDDING_MODEL", "text-embedding-3-small"))
    temperature: float = field(default_factory=lambda: float(_env("EMPORIO_TEMPERATURE", "0.2")))
    db_path: Path = field(
        default_factory=lambda: Path(_env("EMPORIO_DB_PATH", str(VAR_DIR / "emporio.sqlite"))))

    def require_openai_key(self) -> str:
        if not self.openai_api_key:
            raise RuntimeError(
                "OPENAI_API_KEY is not set. Copy .env.example to .env and fill in your key.")
        return self.openai_api_key


settings = Settings()
