# Irdi Caushaj
from flask import Flask, request, jsonify

app = Flask(__name__)

courses_list = []

courses_dictionary = {
    "id": 1,
    "name": "Python"
    }

def courses_post():
    courses_list.append(courses_dictionary)
    return "OK"

def courses_get():
    return jsonify(courses_list)

@app.route('/courses', methods=['GET','POST'])
def courses():
    if request.method == "POST":
        return courses_post()
    return courses_get()