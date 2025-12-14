from typing import Dict, List

from project_00.constants import DATASET
from project_00.people import PEOPLE_TABLE
from shared.authentication import check_auth

from . import data, database


def ensure_dataset(dataset: str) -> None:
    if not database.dataset_exists(dataset):
        database.create_dataset(dataset)


def ensure_table() -> None:
    if not database.table_exists(DATASET, PEOPLE_TABLE):
        database.create_table(DATASET, PEOPLE_TABLE)


def load_data() -> None:
    rows = data.generate_rows(10)
    database.insert_rows(DATASET, PEOPLE_TABLE, rows)


def show_sample_query() -> List[Dict]:
    query = f"""
        SELECT country, COUNT(*) AS total
        FROM `{database.table_ref(DATASET, PEOPLE_TABLE)}`
        GROUP BY country
        ORDER BY total DESC
    """
    return database.run_query(query)


def display_result(result: List[Dict]) -> None:
    for row in result:
        print(row)


def main() -> None:
    print("Authenticating to the database...")
    check_auth()
    print("Ensuring dataset exists...")
    ensure_dataset(DATASET)
    print("Ensuring table exists...")
    ensure_table()
    print("Loading data into the table...")
    load_data()
    print("Running sample query...")
    result = show_sample_query()
    print("Query Results:")
    display_result(result)


if __name__ == "__main__":
    main()
