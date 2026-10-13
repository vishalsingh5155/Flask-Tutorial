from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

@app.route('/about')
def about():
    return "Welcome to the About Page!"

@app.route('/contact')
def contact():
    return "This is the Contact Page!"


if __name__ == '__main__':
    app.run(debug=True)