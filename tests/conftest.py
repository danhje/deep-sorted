from datetime import datetime

import pytest


@pytest.fixture()
def ordered_structs():
    return [
        [-3, -2, -1, 0, 1, 2, 3],
        {"a": 1, "b": 2, "c": [1, 2, 3]},
        {-999: ValueError, -1: ..., False: ..., True: ..., 999: ..., None: ...},
        {
            "books": [
                {
                    "editions": {
                        1: "First Edition",
                        datetime(2019, 5, 7, 0, 0): "Second Edition",
                        "0": "Draft Edition",
                    },
                    "id": 125,
                    "published": datetime(2019, 5, 7, 0, 0),
                    "title": "Exhalation",
                },
                {
                    "id": 124,
                    "published": datetime(1991, 8, 1, 0, 0),
                    "title": "Understand",
                    "ratings": (0, 0, 3, 5, 6, 6, 6, 6, 6),
                },
            ],
            "id": 9,
            "name": "Ted Chiang",
        },
    ]
