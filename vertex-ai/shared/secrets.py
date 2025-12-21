from dataclasses import fields
from email.policy import default
from logging import config
import tomllib
from pathlib import Path
from typing import List, Optional, Any

CONFIG_PATH = Path("secrets/secrets.toml")

# ---


def load_toml(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open("rb") as f:
        return tomllib.load(f)


def get_field_str(fields: List[str], default_value: Optional[str] = None) -> Any:
    current = load_toml(CONFIG_PATH)
    for field in fields:
        current = current.get(field, {})
        if current == {} and default_value is not None:
            return default_value
    return current


def get_api_key_path(config: dict) -> Path:
    return Path(config.get("paths", {}).get("api_key_path", DEFAULT_API_KEY_PATH))


def read_secret(path: Path) -> str:
    return path.read_text().strip()


def load_vertex_ai_api_key() -> str:
    config = load_toml(CONFIG_PATH)
    path = get_api_key_path(config)
    return read_secret(path)

# ---


DEFAULT_API_KEY_PATH = Path("/etc/secrets/vertex-ai.json")
DEFAULT_LOCATION = "us-central1"
DEFAULT_PROJECT_ID = None

VERTEX_AI_API_KEY: str = load_vertex_ai_api_key()
LOCATION: str = get_field_str(
    ["project", "location"], DEFAULT_LOCATION)
PROJECT_ID: str = get_field_str(
    ["project", "project_id"], DEFAULT_PROJECT_ID)
