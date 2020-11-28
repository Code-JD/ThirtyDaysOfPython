from flask import Flask

app = Flask(__name__)

#http://localhost:8000/
@app.route("/", methods=['GET'])
def hello_world():
	return "Hello, world.  This is Flask"

#http://localhost:8000/
@app.route("/abc", methods=['GET'])
def abcview():
	return "Hello, world.  This is Flask"