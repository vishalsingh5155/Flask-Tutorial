from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

@app.route('/users')
def users():
    return "Welcome to the Users Page!"


@app.route('/user/<name>')
def user(name):
    return f"Hello, {name}!"

@app.route('/student/<name>/<course>')
def student(name, course):
    return f"Hello {name}, you are enrolled in the {course} course."


if __name__ == '__main__':
    app.run(debug=True, port=5001)