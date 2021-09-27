from typing import List
from src.jobs import read


def reduce_filter(acc: list, current, column: str) -> list:
    column_type = str(current[column])
    if acc.count(column_type) == 0 and column_type != "":
        acc.append(column_type)
        return acc
    return acc


def filter_types(data: List[dict], type_filter: str) -> list:
    acc = []
    temp = []
    for item in data:
        temp = reduce_filter(acc, item, type_filter).copy()
        acc.clear()
        acc = temp.copy()
        temp.clear()
    return acc


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs_data = read(path)

    return filter_types(jobs_data, "job_type")


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    industry_data = read(path)

    return filter_types(industry_data, "industry")


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    data = read(path)
    salary_max = [
        int(row["max_salary"]) for row in data if row["max_salary"].isdigit()
    ]
    return max(salary_max)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    data = read(path)
    salary_min = [
        int(row["min_salary"]) for row in data if row["min_salary"].isdigit()
    ]
    return min(salary_min)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Salary error!!!")

    elif (
        not isinstance(job["max_salary"], int)
        or not isinstance(job["min_salary"], int)
        or not isinstance(salary, int)
    ):
        raise ValueError("Salary invalid!!!")

    elif job["min_salary"] > job["max_salary"]:
        raise ValueError("Minimum wage greater than maximum wage")

    elif salary is None:
        raise ValueError("Salary is not defined")

    else:
        return salary >= job["min_salary"] and salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    jobs_result = list()
    MIN_SALARY_LOCAL = "min_salary"
    MAX_SALARY_LOCAL = "max_salary"
    for job in jobs:
        job_temp = dict()
        job_temp[MIN_SALARY_LOCAL] = job[MIN_SALARY_LOCAL]
        job_temp[MAX_SALARY_LOCAL] = job[MAX_SALARY_LOCAL]
        try:
            if matches_salary_range(job_temp, salary):
                jobs_result.append(job)
            job_temp.clear()
        except (RuntimeError, TypeError, NameError, ValueError):
            pass

    return jobs_result
