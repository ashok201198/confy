class ApiException(BaseException):

    def __init__(self, message="Exception!!"):
        self.message = message

    def __repr__(self):
        return self.message


class NoRecordFoundException(ApiException):

    def __init__(self, message="No record found of type {}", params=()):
        self.message = message.format(params)


class CantScheduleException(ApiException):

    def __init__(self, message="Unable to schedule {}", params=()):
        self.message = message.format(params)


class AlreadyRegisteredException(ApiException):

    def __init__(self, message="Already registered", params=()):
        self.message = message.format(params)


class CantUpdateFieldException(ApiException):

    def __init__(self, message="Can't update the field {}", params=()):
        self.message = message.format(params)
