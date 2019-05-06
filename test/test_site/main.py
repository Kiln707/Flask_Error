from flask import Flask, render_template, abort

def callback(code, trace, error, request):
    print(code)
    print(error)
    for line in trace:
        print(line)
    print(request)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='meh'
    #All other setup
    from flask_error import FlaskError
    error = FlaskError(app, template='hub.html')
    return app

def endpoints():
    rules = [rule.endpoint for rule in app.url_map.iter_rules() if rule.endpoint != 'static']
    return rules

def _ctx():
    return dict(endpoints=endpoints)

if __name__ == '__main__':
    import sys, os
    package=os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    sys.path.insert(0,package)
    app = create_app()
    app.config['TESTING']=True
    app.context_processor(_ctx)

    @app.route('/')
    def root():
        return render_template('hub.html')

    @app.route('/error')
    def error():
        raise Exception("What do you mean it broke?")

    @app.route('/ioerror')
    def ioerror():
        f = open('doesnotexist')

    @app.route('/abort500')
    def fiveoo():
        abort(500)

    @app.route('/abort400')
    def fouroo():
        abort(400)

    @app.route('/notfound')
    def notfound():
        abort(404)

    app.run()
