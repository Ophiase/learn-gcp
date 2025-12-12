import random
from pprint import pprint
from typing import Dict, List

import constants
from people import People


def random_choice(values: List[str]) -> str:
    return random.choice(values)


def generate_row() -> People:
    return People(
        first_name=random_choice(constants.FIRST_NAMES),
        last_name=random_choice(constants.LAST_NAMES),
        country=random_choice(constants.COUNTRIES),
        age=random.randint(constants.AGE_RANGE[0], constants.AGE_RANGE[1]),
    )


def generate_rows(n: int) -> List[People]:
    return [generate_row() for _ in range(n)]


if __name__ == "__main__":
    sample_data = generate_rows(5)
    pprint(sample_data)
