import pytest
from src.pre_built.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {
            "title": "Alquimista",
            "date_posted": "2023-03-20",
            "max_salary": 2000,
            "min_salary": 1100,
        },
        {
            "title": "Pescador",
            "date_posted": "2023-03-21",
            "max_salary": 2100,
            "min_salary": 1200,
        },
        {
            "title": "Padeiro",
            "date_posted": "2023-03-22",
            "max_salary": 2200,
            "min_salary": 1300,
        },
    ]


def test_sort_by_criteria(jobs):

    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == 1100

    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == 2200

    sort_by(jobs, "date_posted")
    assert jobs[0]["date_posted"] == "2023-03-22"
