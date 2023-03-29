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
    filter = list()
    for job in jobs:
        if job["job_type"] == job_type:
            filter.append(job)
    return filter
