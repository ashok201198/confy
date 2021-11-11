from datetime import datetime, timedelta

from confyapp.exceptions import ApiException

time_format = "%Y-%m-%dT%H:%M:%S"


def before_talk_insert_or_update(mapper, connection, target):
    if target.start_date is None:
        raise ApiException("Should provide start_date")
    start_date = datetime.strptime(target.start_date, time_format)
    if start_date < datetime.now():
        raise ApiException("start_date should be in the future")
    if target.end_date is None:
        if target.duration is None:
            raise ApiException("Should provide at least end_date or duration")
        else:
            target.end_date = (start_date + timedelta(minutes=target.duration)).strftime(time_format)
    else:
        end_date = datetime.strptime(target.end_date, time_format)
        total_mins = (end_date - start_date).seconds // 60
        target.duration = total_mins


def before_conference_insert_or_update(mapper, connection, target):
    if target.start_date is None:
        raise ApiException("Should provide start_date")
    start_date = datetime.strptime(target.start_date, time_format)
    if start_date < datetime.now():
        raise ApiException("start_date should be in the future")
    if target.end_date is None:
        print("Assuming 2 days")
        target.end_date = (start_date + timedelta(days=2)).strftime(time_format)
