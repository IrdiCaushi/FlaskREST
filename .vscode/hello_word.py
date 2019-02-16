# Irdi Caushaj
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/hello/<word>')
def hello_word(word):
    return "Hello {}".format(word)


my_courses = [
    {"id": 1, "name": "COS300"},
    {"id": 2, "name": "COS400"}
]


def get_courses(course_id):
    for course in my_course:
        if course["id"] == course_id:
            return jsonify(course)
    else:
        return {"course": None}

def post_courses(course_id):
    my_courses_dict({"id": course_id, "name":})
    my_courses.append(my_courses_dict)



@app.route('/courses/<int:id>', methods=['GET','POST'])
def courses(id, name):
    if request.method == "POST":
        return post_courses()
    return get_courses()


@app.route('/hello_v2/', methods=['POST'])
def hello_word_v2():
    data = request.get_json()
    word = data['word']
    return "Hello {}".format(word)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        return "Buy, World"
    return "Hello, World"