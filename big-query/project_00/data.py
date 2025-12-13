import random
from pprint import pprint
from typing import Dict, List

from .constants import AGE_RANGE, COUNTRIES, FIRST_NAMES, LAST_NAMES
from .people import People


def random_choice(values: List[str]) -> str:
    return random.choice(values)


def generate_row() -> People:
    return People(
        first_name=random_choice(FIRST_NAMES),
        last_name=random_choice(LAST_NAMES),
        country=random_choice(COUNTRIES),
        age=random.randint(AGE_RANGE[0], AGE_RANGE[1]),
    )


def generate_rows(n: int) -> List[People]:
    return [generate_row() for _ in range(n)]


if __name__ == "__main__":
    sample_data = generate_rows(5)
    pprint(sample_data)
