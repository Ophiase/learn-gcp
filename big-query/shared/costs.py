from pathlib import Path

from google.cloud import bigquery

from .constants import DATASET_LOCATION


def estimate_query_cost(client: bigquery.Client, sql: str) -> float:
    job_config = bigquery.QueryJobConfig(dry_run=True, use_query_cache=False)
    job = client.query(sql, job_config=job_config)
    return bytes_to_dollars(job.total_bytes_processed)


def bytes_to_dollars(bytes_processed: int) -> float:
    return bytes_processed / 1_000_000_000_000 * 5
