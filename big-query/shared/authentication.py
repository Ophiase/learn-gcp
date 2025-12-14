import json

from google.cloud import bigquery

from shared.secrets import BIG_QUERY_API_KEY


def get_client() -> bigquery.Client:
    info = json.loads(BIG_QUERY_API_KEY)
    client = bigquery.Client.from_service_account_info(info)
    return client


def check_auth() -> None:
    try:
        client = get_client()
        client.project  # Trigger an API call to verify authentication
    except Exception as e:
        raise RuntimeError(
            "Authentication failed. Please check your Google Cloud credentials."
        ) from e
