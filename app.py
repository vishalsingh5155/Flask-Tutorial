from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

#This route will accept an integer parameter in the URL
@app.route('/user/<int:id>')
def user(id):
    return f"User id: {id}"

#This route will accept a float parameter in the URL
@app.route('/price/<float:amount>')
def price(amount):
    return f"Price: ${amount}"

#This route will accept a string parameter in the URL
#String parameters can include letters, numbers, and underscores
#String is the default type for route parameters, so you can also omit the type and just use <username>
@app.route('/users/<string:username>')
def users(username):
    return f"Hello, {username}!"

#Path parameters can also be used to capture a path-like structure in the URL.
#Path will capture everything after the specified route, including slashes. This is useful for capturing file paths or other hierarchical data.
@app.route('/files/<path:file_path>')
def files(file_path):
    return file_path

#This route will accept a UUID parameter in the URL
#UUID is a standardized 128-bit format for a string ID that is unique across both time and space. It is often used to identify resources in distributed systems.
@app.route('/student/<uuid:user_id>')
def student(user_id):
    return f"Student ID: {user_id}"

if __name__ == '__main__':
    app.run(debug=True, port=5001)