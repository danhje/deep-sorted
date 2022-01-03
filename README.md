# deep-sorted

![Testing and linting](https://github.com/danhje/deep-sorted/workflows/Test%20And%20Lint/badge.svg)
[![codecov](https://codecov.io/gh/danhje/deep-sorted/branch/master/graph/badge.svg)](https://codecov.io/gh/danhje/deep-sorted)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/danhje/deep-sorted?include_prereleases)
![PyPI](https://img.shields.io/pypi/v/deep-sorted)

## Motivation

When validating parsed JSON objects, schemas and other nested data structures in unit tests, order
is typically not important. And yet I often find myself manually sorting the target structures
when the internals of the tested function is modified such that order is changed. With this package,
both the target and the actual structure can be recursively sorted before comparison.

## Installation

Using poetry:

```shell
poetry add deep-sorted
```

Using pipenv:

```shell
pipenv install deep-sorted
```

Using pip:

```shell
pip install deep-sorted
```

## Usage

```python
from deep_sorted import deep_sorted
from datetime import datetime

one = {
    "id": 9,
    "name": "Ted Chiang",
    "books": [
        {
            "id": 124,
            "published": datetime(1991, 8, 1, 0, 0),
            "title": "Understand",
            "ratings": (6, 6, 3, 5, 6, 6, 0, 6, 0),
        },
        {
            "id": 125,
            "published": datetime(2019, 5, 7, 0, 0),
            "title": "Exhalation",
        },
    ],
}

two = {
    "books": [
        {
            "published": datetime(2019, 5, 7, 0, 0),
            "title": "Exhalation",
            "id": 125,
        },
        {
            "ratings": (3, 0, 0, 6, 6, 6, 6, 5, 6),
            "id": 124,
            "published": datetime(1991, 8, 1, 0, 0),
            "title": "Understand",
        },
    ],
    "id": 9,
    "name": "Ted Chiang",
}

assert deep_sorted(one) == deep_sorted(two)
```
