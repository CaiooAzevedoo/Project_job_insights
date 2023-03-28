from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        header, *data = csv.reader(file)
    file_list = list()
    for row in data:
        file_dict = dict()
        for index, item in enumerate(row):
            file_dict[header[index]] = item
        file_list.append(file_dict)
    return file_list


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    job_types = list()
    for job in jobs:
        job_types.append(job['job_type'])
    return list(set(job_types))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
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
    raise NotImplementedError
