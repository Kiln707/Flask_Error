from flask import request, response


class ErrorsException(Exception):
    def __init__(self, status_code, message, *args, **kwargs):
        self.status_code=0
        self.message=message
        self.request = kwargs['request'] if kwargs['request'] else request
        self.response = kwargs['response'] if kwargs['response'] else response

class ClientError(ErrorsException):
    pass

class ClientBadRequest(ClientError):
    def __init__(self)
