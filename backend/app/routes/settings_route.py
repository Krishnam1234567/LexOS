"""
LexOS — Settings API
Persistent settings using SQLite.
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any
from app.db.sqlite_db import get_conn
import json

router = APIRouter(prefix="/settings", tags=["Settings"])


class SettingsSaveRequest(BaseModel):
    section: str
    data: dict[str, Any]


@router.get("/")
async def get_settings():
    """Get all settings from database."""
    conn = get_conn()
    rows = conn.execute("SELECT section, data FROM settings").fetchall()
    conn.close()
    return {row["section"]: json.loads(row["data"]) for row in rows}


@router.post("/")
async def save_settings(req: SettingsSaveRequest):
    """Save settings for a specific section."""
    conn = get_conn()
    conn.execute(
        "INSERT OR REPLACE INTO settings (section, data) VALUES (?, ?)",
        (req.section, json.dumps(req.data))
    )
    conn.commit()
    conn.close()
    return {"status": "saved", "section": req.section, "data": req.data}
