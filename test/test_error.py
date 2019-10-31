from flask import abort
from flask_error import FlaskError
import sys

def test_callback(app):
    errorcode = 500
    def callback_test(code, error, trace, request, **kwargs):
        print(code, error, trace, request,**kwargs)
        assert code == errorcode
    @app.route('/500')
    def test_route1():
        abort(errorcode)

    @app.route('/exception')
    def test_route2():
        raise KeyError()

    @app.route('/404')
    def test_route3():
        abort(404)

    error = FlaskError(app, callback=[callback_test])
    client = app.test_client()
    try:
        print(client.get('/500', follow_redirects=True))
        print(client.get('/exception', follow_redirects=True))
        client.get('/404', follow_redirects=True)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        assert False
