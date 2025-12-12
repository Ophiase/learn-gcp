from typing import Dict, List

from google.cloud import bigquery


def client() -> bigquery.Client:
    return bigquery.Client()


def check_auth() -> None:
    try:
        client = bigquery.Client()
        client.project  # Trigger an API call to verify authentication
    except Exception as e:
        raise RuntimeError(
            "Authentication failed. Please check your Google Cloud credentials.") from e


def table_ref(dataset: str, table: str) -> str:
    return f"{client().project}.{dataset}.{table}"


def table_exists(dataset: str, table: str) -> bool:
    try:
        client().get_table(table_ref(dataset, table))
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
    client().create_table(table_obj)


def insert_rows(dataset: str, table: str, rows: List[Dict[str, str]]) -> None:
    table_id = table_ref(dataset, table)
    client().insert_rows_json(table_id, rows)


def run_query(query: str) -> List[Dict]:
    return list(client().query(query).result())
