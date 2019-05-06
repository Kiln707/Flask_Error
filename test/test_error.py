from flask import abort
from flask_error import FlaskError

def test_callback(app):
    called=False
    def callback_test(code, error, trace, request, **kwargs):
        print('callback')
        global called
        called=True
    @app.route('/')
    def test_route():
        abort(500)

    FlaskError(app, callback=callback_test)
    client = app.test_client()
    try:
        client.get('/', follow_redirects=True)
    except:
        pass
    assert called, 'not called'
