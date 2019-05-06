# Flask_Error

A simple and easy to use Error/Exception Management for Flask.

Set it and forget it approach, while allowing customization. Don't worry about accidentally leaking code.

Flask Error is designed to catch all errors from code Exceptions or abort(), providing easy to use features for quality of life and faster development.

### Quickstart

```python
app = Flask(__name__)
from flask_error import FlaskError
FlaskError(app)
```
That's it.

Users will get a simple error code and message if something goes wrong.

### Callback Feature

By Using the callback feature, when an error occurs, a function with the relevant information will be called.
Use this to send an email to an administrator, log the exception, etc.

Simply create a function to be called and pass it to the constructor
```python
def error_callback(code, error, trace, request, **kwargs):
  print(code, error, trace, request)
  #Log it, mail it, etc.

app = Flask(__name__)
from flask_error import FlaskError
FlaskError(app, callback=error_callback)
```

Objects are, error = Exception object, Trace = List of traceback message lines, request = Flask Request object



### Troubleshooting and Testing Feature

For troubleshooting and testing purposes, the error code, exception, traceback, and request may be rendered on the template.
To do this, simply set Flask's Testing config property to True.

NOTE: This is insecure! This feature is only intended for developers testing their site and NOT FOR PRODUCTION!

```python
app = Flask(__name__)
from flask_error import FlaskError
FlaskError(app)
app.config['TESTING']=True
```



### Configuring Error Messages

To customize error messages add to the app config the error message like below:

```python
app = Flask(__name__)
from flask_error import FlaskError
FlaskError(app)
app.config['ERROR_404']='Whatever you are looking for is not here!'
```

Create custom errors+messages by using a non standard error code:

```python
app = Flask(__name__)
from flask_error import FlaskError
FlaskError(app)
app.config['ERROR_480']='Custom Error!'
```

Configuration format is ['ERROR_(Error Code)'] = 'Message'



### Changing the Template

It is highly recommended to use a custom template as the default is not pretty.
Both Testing and production renders the same template. It is advised to use the following format in template:

```HTML
<h1>{{ code }}</h1> <!-- Display the error code -->
<p>{{ message }}</p> <!-- Display your error message -->
{% if error %}      <!-- Check if error or trace is present, This means app is in testing mode -->
  <h2>Traceback</h2>
  {{ error }}   <!-- Exception object. This will get the __repr__ of the exception -->
  <p>{% for line in trace %} <!-- traceback. Trace back is a list of each line. For better readability, it is recommended to loop -->
      {{ line }}</br>
  {%endfor%}</p>
  <h2>Request</h2>
  <p>{{ request }}</p> <!-- Request object. This will get the __repr__ of the request -->
{% endif %}
```

For Flask Error to use the template, pass the template path in the constructor

```python
app = Flask(__name__)
from flask_error import FlaskError
FlaskError(app, tempalte='error.html')
```
