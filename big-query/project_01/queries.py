from dataclasses import dataclass
from pathlib import Path
from typing import List

from google.cloud import bigquery

from shared.costs import estimate_query_cost

from .constants import QUERIES_DIR


@dataclass
class QueryConfig:
    name: str
    sql_file_name: str
    description: str = ""


QUERIES: List[QueryConfig] = [
    QueryConfig(
        "extreme weather frequency by year", "extreme_weather_frequency_by_year.sql"
    ),
    QueryConfig("filter and aggregation", "filter_and_aggregation.sql"),
    QueryConfig("weather anomaly detection", "weather_anomaly_detection.sql"),
    QueryConfig("Seasonal temperature profiles", "seasonal_temperature_profiles.sql"),
    QueryConfig("Correlation between temperature and precipitation", "correlation.sql"),
]


def execute_a_single_query(
    client: bigquery.Client,
    query: QueryConfig,
    queries_dir: Path = QUERIES_DIR,
    dry_run: bool = False,
) -> None:
    print(f"[QUERY] Executing: {query.name}")

    query_path = queries_dir / query.sql_file_name
    with open(query_path, "r") as file:
        sql = file.read()

    if dry_run:
        estimated_cost = estimate_query_cost(client, sql)
        print(
            f"[DRY RUN] Estimated cost for query '{query.name}': ${estimated_cost:.6f}"
        )
        print("-" * 40)
        return

    query_job = client.query(sql)
    results = query_job.result()
    print(f"Results for {query.name}:")
    for row in results:
        print(dict(row))

    print("-" * 40)


def execute_queries(
    client: bigquery.Client,
    queries: List[QueryConfig] = QUERIES,
    queries_dir: Path = QUERIES_DIR,
    dry_run: bool = False,
) -> None:
    for query in queries:
        execute_a_single_query(client, query, queries_dir, dry_run)
