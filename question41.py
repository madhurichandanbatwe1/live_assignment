# To create a Flask route that accepts a parameter in the URL and displays it on the page, you can use the Flask route decorator with URL parameters.

from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def hello_name(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)

