import csv
from typing import List


def read(path: str) -> List[dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """

    #  esse código estava com algum comportamemto estranho
    # result = list()
    # with open(path) as jobs_file:
    #     header, *jobs_list = csv.reader(jobs_file)
    #     for job in jobs_list:
    #         temp_job = dict()
    #         for index in range(len(job)):
    #             temp_job[header[index]] = job[index] or "Uninformed"
    #         result.append(temp_job)
    # return result

    with open(path) as file:
        list_file = csv.DictReader(file, delimiter=",", quotechar='"')
        return list(list_file)
