import os
import tempfile

import pytest

from flask import Flask
from flask_error import FlaskError

@pytest.fixture()
def app(request):
    app = Flask(__name__)
    app.config['DEBUG']=True
    app.config['TESTING']=True
    app.config['SECRET_KEY']='secret'
    return app
