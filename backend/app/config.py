"""
LexOS — Centralized Configuration
Reads from environment variables with sensible local defaults.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application-wide settings loaded from env vars."""

    # ── App ───────────────────────────────────
    APP_NAME: str = "LexOS"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True
    GOOGLE_CLIENT_ID: str | None = None



    # ── AI Models ─────────────────────────────
    GEMINI_API_KEY: str | None = None
    GEMINI_API_KEY_1: str | None = None
    GEMINI_API_KEY_2: str | None = None
    GEMINI_API_KEY_3: str | None = None
    GEMINI_API_KEY_4: str | None = None
    GEMINI_API_KEY_5: str | None = None
    GEMINI_API_KEY_6: str | None = None
    GEMINI_API_KEY_7: str | None = None
    GEMINI_API_KEY_8: str | None = None
    GEMINI_API_KEY_9: str | None = None
    GEMINI_API_KEY_10: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def api_keys(self) -> list[str]:
        keys = [
            self.GEMINI_API_KEY_1, self.GEMINI_API_KEY_2, self.GEMINI_API_KEY_3,
            self.GEMINI_API_KEY_4, self.GEMINI_API_KEY_5, self.GEMINI_API_KEY_6,
            self.GEMINI_API_KEY_7, self.GEMINI_API_KEY_8, self.GEMINI_API_KEY_9,
            self.GEMINI_API_KEY_10, self.GEMINI_API_KEY
        ]
        valid_keys = [k for k in keys if k and k != "your_gemini_api_key_here"]
        # Deduplicate while preserving order
        return list(dict.fromkeys(valid_keys))


settings = Settings()
