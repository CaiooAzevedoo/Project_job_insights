from typing import List, Dict
from . import jobs


def get_unique_industries(path: str) -> List[str]:
    jobs_registered = jobs.read(path)
    jobs_industry = list()
    for job in jobs_registered:
        jobs_industry.append(job['industry'])
    return list(set(jobs_industry))


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
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
    raise NotImplementedError
