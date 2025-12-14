from typing import TypedDict

PEOPLE_TABLE = "people"


class People(TypedDict):
    first_name: str
    last_name: str
    country: str
    age: int
