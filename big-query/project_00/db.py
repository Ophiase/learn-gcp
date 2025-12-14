from collections.abc import Sequence
from typing import Any, Dict, List, Mapping
import json

from google.cloud import bigquery

from .secrets import BIG_QUERY_API_KEY


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


def dataset_ref(dataset: str) -> str:
    return f"{get_client().project}.{dataset}"


def dataset_exists(dataset: str) -> bool:
    try:
        get_client().get_dataset(dataset_ref(dataset))
        return True
    except:
        return False


def create_dataset(dataset: str) -> None:
    dataset_obj = bigquery.Dataset(dataset_ref(dataset))
    get_client().create_dataset(dataset_obj)


def table_ref(dataset: str, table: str) -> str:
    return f"{get_client().project}.{dataset}.{table}"


def table_exists(dataset: str, table: str) -> bool:
    try:
        get_client().get_table(table_ref(dataset, table))
        return True
    except:
        return False


def create_table(dataset: str, table: str) -> None:
    schema = [
        bigquery.SchemaField("first_name", "STRING"),
        bigquery.SchemaField("last_name", "STRING"),
        bigquery.SchemaField("country", "STRING"),
        bigquery.SchemaField("age", "INTEGER"),
    ]
    table_obj = bigquery.Table(table_ref(dataset, table), schema=schema)
    get_client().create_table(table_obj)


def insert_rows(dataset: str, table: str, rows: Sequence[Mapping[Any, Any]]) -> None:
    table_id = table_ref(dataset, table)
    get_client().insert_rows_json(table_id, rows)


def run_query(query: str) -> List[Dict]:
    return list(get_client().query(query).result())
