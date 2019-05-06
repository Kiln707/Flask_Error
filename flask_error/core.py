from flask import response, render_template
from .exceptions import ErrorsException

class FlaskError():
    def __init__(self, app, template='error/error.html', callback=None):
        self.app=app
        self.testing = app.config['TESTING']
        self.debug = app.config['DEBUG']
        self.template=template
        self.callback=callback
        app.register_error_handler(BaseException, self.handle_error)


    #   Get a stacktrace on the exception that occoured.
    #   This may be used for troubleshooting purposes.
    def getErrorInfo():
        return ''.join(traceback.format_list(traceback.extract_tb(sys.exc_info()[2]))) # Get a string of the stack trace

    def get_message(self, code):
        pass

    def handle_error(self, error):
        code = None
        if hasattr(error, 'status_code'):
            code = getattr(error, 'status_code')
        elif hasattr(error, 'code'):
            code = getattr(error, 'code')
        else:
            code=500
        trace = self.getErrorInfo()
        if self.callback:
            self.callback(code=code, trace=trace, error=error, response=response)
        if self.testing or self.debug:
            return render_template(self.template, code=code, message=message, trace=trace, response=response)
        return render_template(self.template, code=code, message=self.get_message(code))
