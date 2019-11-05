from flask import Blueprint, render_template, request
from werkzeug.local import LocalProxy
from werkzeug.exceptions import HTTPException
import sys, traceback
from .config import default_config
from .exceptions import *

class FlaskError(Blueprint):
    def __init__(self, app, blueprint_name='error', url_prefix='/error', subdomain='', template_folder='templates/error', callback=[]):
        app.extensions['Error']=self
        self.debug = LocalProxy(lambda:app.config['DEBUG'])
        self.config = LocalProxy(lambda: app.config)
        for key, value in default_config.items():
            app.config.setdefault('ERROR_'+key, value)
        if not isinstance(callback, list):
            raise ValueError("Callback must be a list")
        self.callback=callback
        for cls in HTTPException.__subclasses__():
            app.register_error_handler(cls, self.handle_error)
        for code in range(400, 599):
            try:
                app.register_error_handler(code, self.handle_error)
            except KeyError:
                pass
        app.register_error_handler(Exception, self.handle_error)
        self._register_blueprint(app=app, blueprint_name=blueprint_name, url_prefix=url_prefix, subdomain=subdomain, template_folder=template_folder)

    def _register_blueprint(self, app, blueprint_name, url_prefix, subdomain, template_folder):
        bp = Blueprint(blueprint_name,
                    __name__,
                    url_prefix=url_prefix,
                    subdomain=subdomain,
                    template_folder=template_folder)
        app.register_blueprint(bp)


    #   Get a stacktrace on the exception that occoured.
    #   This may be used for troubleshooting purposes.
    def getErrorInfo(self):
        return traceback.format_list(traceback.extract_tb(sys.exc_info()[2]))

    def get_message(self, code):
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
        for call in self.callback:
            call(code=errorcode, error=error, trace=trace, request=request)
        returndata = {}
        if self.debug:
            returndata = {'code': errorcode, 'message': message, 'error': error, 'trace': trace, 'request': request}
        else:
            returndata = {'code': errorcode, 'message': message}
        if request.is_json:
            return jsonify(returndata), errorcode
        return render_template('error.html', **returndata), errorcode
