from requests.exceptions import RequestException
from .exceptions import ErrorsException

class FlaskError():
    def __init__(self, app, callback):
        self.app=app
        self.callback=callback
        app.register_error_handler(BaseException, self.handle_error)

    def handle_error(self, error):
        try:
            if isinstance(error, ErrorsException):
                raise
            elif isinstance(error, RequestException):
                #Convert RequestException to ErrorsException
                
