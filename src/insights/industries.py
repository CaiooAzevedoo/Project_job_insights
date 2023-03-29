from typing import List, Dict
from . import jobs


def get_unique_industries(path: str) -> List[str]:
    jobs_registered = jobs.read(path)
    jobs_industry = list()
    for job in jobs_registered:
        if job["industry"] != "":
            jobs_industry.append(job["industry"])
    return list(set(jobs_industry))


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filter = list()
    for job in jobs:
        if job["industry"] == industry:
            filter.append(job)
    return filter
