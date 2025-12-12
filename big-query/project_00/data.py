import random
from typing import Dict, List
from people import People
import constants
from pprint import pprint


def random_choice(values: List[str]) -> str:
    return random.choice(values)


def generate_row() -> People:
    return People(
        first_name=random_choice(constants.FIRST_NAMES),
        last_name=random_choice(constants.LAST_NAMES),
        country=random_choice(constants.COUNTRIES),
    )


def generate_rows(n: int) -> List[People]:
    return [generate_row() for _ in range(n)]


if __name__ == "__main__":
    sample_data = generate_rows(5)
    pprint(sample_data)
