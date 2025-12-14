import tomllib
from pathlib import Path

DEFAULT_API_KEY_PATH = Path("/etc/secrets/big-query.json")
CONFIG_PATH = Path("secrets/secrets.toml")


def load_toml(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open("rb") as f:
        return tomllib.load(f)


def get_api_key_path(config: dict) -> Path:
    return Path(config.get("paths", {}).get("api_key_path", DEFAULT_API_KEY_PATH))


def read_secret(path: Path) -> str:
    return path.read_text().strip()


def load_big_query_api_key() -> str:
    config = load_toml(CONFIG_PATH)
    path = get_api_key_path(config)
    return read_secret(path)


BIG_QUERY_API_KEY: str = load_big_query_api_key()
