from src.sorting import sort_by
import pytest
from datetime import date


job_mock = [
    {
        "title": "Web developer",
        "min_salary": "",
        "date_posted": date(2020, 5, 8),
        "id": 0,
    },
    {
        "title": "Front end developer",
        "max_salary": "31000",
        "min_salary": "21000",
        "date_posted": date(2020, 5, 2),
        "id": 1,
    },
    {
        "title": "Back end developer",
        "max_salary": "25000",
        "min_salary": "",
        "date_posted": date(2021, 8, 8),
        "id": 2,
    },
    {
        "title": "Full stack end developer",
        "max_salary": "25367",
        "min_salary": "21058",
        "date_posted": date(2020, 1, 17),
        "id": 3,
    },
    {
        "title": "Full stack end developer",
        "max_salary": "25369",
        "min_salary": "18058",
        "date_posted": date(2020, 1, 15),
        "id": 4,
    },
    {
        "title": "Full stack end developer",
        "max_salary": "",
        "min_salary": "21758",
        "date_posted": date(2021, 2, 15),
        "id": 5,
    },
]

expected_1_max = [
    job_mock[1],
    job_mock[4],
    job_mock[3],
    job_mock[2],
    job_mock[0],
    job_mock[5],
]

expected_1_min = [
    job_mock[4],
    job_mock[1],
    job_mock[3],
    job_mock[5],
    job_mock[2],
    job_mock[0],
]

expected_1_date = [
    job_mock[4],
    job_mock[1],
    job_mock[3],
    job_mock[5],
    job_mock[2],
    job_mock[0],
]

excepted = [expected_1_max, expected_1_min, expected_1_date]

excepted_error = "0x0x0x0x0x"
criteria_type = ["max_salary", "min_salary", "date_posted"]


def test_sort_by_criteria():
    for x_test in range(len(criteria_type)):
        print(criteria_type[x_test])
        sort_by(job_mock, criteria_type[x_test])
        assert job_mock == excepted[x_test]

    with pytest.raises(ValueError):
        sort_by(job_mock, excepted_error)
