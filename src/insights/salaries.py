from typing import Union, List, Dict
from . import jobs


def get_max_salary(path: str) -> int:
    jobs_salary = jobs.read(path)
    job_max_salary = 0
    for job in jobs_salary:
        salary = job["max_salary"]
        if salary not in ['', 'invalid'] and int(salary) > job_max_salary:
            job_max_salary = int(salary)
    return job_max_salary


def get_min_salary(path: str) -> int:
    jobs_salary = jobs.read(path)
    job_min_salary = 1000000
    for job in jobs_salary:
        salary = job["min_salary"]
        if salary not in ['', 'invalid'] and int(salary) < job_min_salary:
            job_min_salary = int(salary)
    return job_min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if int(job["max_salary"]) < int(job["min_salary"]):
            raise ValueError
        return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
    except (KeyError, TypeError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
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
    raise NotImplementedError
