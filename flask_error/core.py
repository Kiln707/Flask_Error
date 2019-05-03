
class FlaskError():
    def __init__(self, app):
        self.app=app
        app.register_error_handler(Exception, handle_error)

    def handle_error(self, error):
        print(error)
