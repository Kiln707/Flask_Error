from flask import render_template, request
from werkzeug.local import LocalProxy
import sys, traceback

from .config import __default_config

class FlaskError():
    def __init__(self, app, template='error/error.html', callback=None):
        self.app=app
        app.error_handler=self
        self.testing = LocalProxy(lambda:app.config['TESTING'])
        self.debug = LocalProxy(lambda:app.config['DEBUG'])
        self.config = LocalProxy(lambda: app.config)
        for key. value in __default_config.items():
            self.app.config.setdefault('ERROR_'+key, value)
        self.template=template
        self.callback=callback
        app.register_error_handler(Exception, self.handle_error)


    #   Get a stacktrace on the exception that occoured.
    #   This may be used for troubleshooting purposes.
    def getErrorInfo(self):
        return traceback.format_list(traceback.extract_tb(sys.exc_info()[2]))

    def get_message(self, code):
        print(code)
        return self.config['ERROR_'+str(code)]

    def handle_error(self, error):
        errorcode = None
        if hasattr(error, 'status_code'):
            errorcode = getattr(error, 'status_code')
        elif hasattr(error, 'code'):
            errorcode = getattr(error, 'code')
        else:
            errorcode=500
        message = self.get_message(errorcode)
        trace = self.getErrorInfo()
        if self.callback:
            self.callback(code=errorcode, error=error, trace=trace, request=request)
        if self.testing or self.debug:
            return render_template(self.template, code=errorcode, message=message, error=error, trace=trace, request=request)
        return render_template(self.template, code=errorcode, message=message)
