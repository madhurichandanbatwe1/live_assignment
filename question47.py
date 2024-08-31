'''Creating a Flask blueprint allows you to organize your Flask application into modules, making it easier to manage and scale. Blueprints help modularize your application by grouping related views, templates, and static files together. Here are the steps to create a Flask blueprint and reasons why you might use one:

Steps to Create a Flask Blueprint:
Create the Blueprint:

Define a new blueprint using flask.Blueprint(name, import_name, url_prefix=None)'''

from flask import Blueprint

# Create a blueprint named 'auth'
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

'''name: The name of the blueprint.
import_name: Typically __name__.
url_prefix: Optional URL prefix for all routes registered with this blueprint.

Define Routes and Views:

Define routes and views specific to the blueprint.'''

@auth_bp.route('/login')
def login():
    return 'Login Page'

@auth_bp.route('/register')
def register():
    return 'Register Page'

'''Register the Blueprint with the Flask Application:

Register the blueprint with the Flask application using app.register_blueprint().'''

from flask import Flask

app = Flask(__name__)

# Register the 'auth' blueprint
from auth import auth_bp
app.register_blueprint(auth_bp)

'''Organize Templates and Static Files:

Create a templates directory and static directory within the blueprint's package or module to keep templates and static files organized.'''


'''project/
├── app.py
├── auth/
│   ├── __init__.py
│   ├── templates/
│   ├── static/
│   └── views.py
└── templates/
Use Blueprint Routes:

Access blueprint routes using the URL prefix specified during blueprint creation or the default / if no prefix is specified.
'''
#<!-- Example of accessing a blueprint route in a template -->
<a href="{{ url_for('auth.login') }}">Login</a>

'''Why Use Flask Blueprints?
Modularity and Organization:

Blueprints help organize your Flask application into logical components (e.g., authentication, admin, API) that can be developed and maintained independently.
Reusability:

Blueprints allow you to reuse routes, templates, and static files across different parts of your application or in multiple applications.
Scalability:

As your application grows, blueprints make it easier to manage and extend functionality without cluttering your main Flask application.
Namespace Management:

Blueprints provide namespace management, allowing you to use the same route names in different blueprints without conflicts.
Testing and Debugging:

Blueprints facilitate easier testing and debugging by isolating specific features or modules within your application.
Collaboration:

Blueprints promote collaboration among team members by defining clear boundaries and responsibilities for different parts of the application.
In summary, Flask blueprints enhance the organization, modularity, and scalability of your Flask applications, making them easier to develop, maintain, and extend as your project grows. They are particularly useful for breaking down large applications into manageable modules and promoting code reuse and collaboration.

'''
