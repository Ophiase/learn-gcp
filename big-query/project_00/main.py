from typing import Dict, List

import data
import db

DATASET = "demo_dataset"
TABLE = "people"


def ensure_table() -> None:
    if not db.table_exists(DATASET, TABLE):
        db.create_table(DATASET, TABLE)


def load_data() -> None:
    rows = data.generate_rows(10)
    db.insert_rows(DATASET, TABLE, rows)


def show_sample_query() -> List[Dict]:
    query = f"""
        SELECT country, COUNT(*) AS total
        FROM `{db.table_ref(DATASET, TABLE)}`
        GROUP BY country
        ORDER BY total DESC
    """
    return db.run_query(query)


def display_result(result: List[Dict]) -> None:
    for row in result:
        print(row)


def main() -> None:
    db.check_auth()
    ensure_table()
    load_data()
    result = show_sample_query()
    display_result(result)


if __name__ == "__main__":
    main()
