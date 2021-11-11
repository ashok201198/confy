from datetime import datetime, timedelta

import ipdb

time_format = "%Y-%m-%dT%H:%M:%S"


def isOverlapping(obj1, obj2):
    # ipdb.set_trace()
    overlap = (obj1[0] < obj2[1]) and (obj2[0] < obj1[1])
    if overlap:
        return -1
    else:
        if obj1[0] > obj2[0]:
            return 1
    return 0


def convertDatetimeToString(date):
    if isinstance(date, str):
        return date
    return date.strftime(time_format)


def convertStringToDatetime(string):
    if isinstance(string, datetime):
        return string
    return datetime.strptime(string, time_format)
