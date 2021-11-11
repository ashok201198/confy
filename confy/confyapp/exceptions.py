class ApiException(BaseException):

    def __init__(self, message="Exception!!"):
        self.message = message

    def __repr__(self):
        return self.message


class NoRecordFoundException(ApiException):

    def __init__(self, message="No record found"):
        self.message = message


class CantScheduleException(ApiException):

    def __init__(self, message="Unable to schedule"):
        self.message = message
