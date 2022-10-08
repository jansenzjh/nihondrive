from json import load
from app import app
from flask import render_template
import csv
import random



class Ques:
    Question = ""
    Answer = ""

    def __init__(self, var1, var2):
        self.Question = var1
        self.Answer = var2

def get_bool(s):
    return s.lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/template')
def template():
    return render_template('home.html')

@app.route('/karimen/<load_all>', methods=['GET', 'POST'])
def karimen(load_all):
    questions = []

    try:
        with open('app/Question.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                questions.append(Ques(row[1], row[4]))

            random.shuffle(questions)
    except Exception as error:
        return str(error)

    if get_bool(load_all):
        return render_template('question_view.html', question_type="karimen all", len=len(questions), questions=questions)
    else:
        return render_template('question_view.html', question_type="karimen", len=len(questions[:50]), questions=questions)

@app.route('/honmen/<load_all>', methods=['GET', 'POST'])
def honmen(load_all):
    questions = []

    try:
        with open('app/Honmen.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                questions.append(Ques(row[1], row[4]))

            random.shuffle(questions)
    except Exception as error:
        return str(error)

    if get_bool(load_all):
        return render_template('question_view.html', question_type="honmen all", len=len(questions), questions=questions)
    else:
        return render_template('question_view.html', question_type="honmen", len=len(questions[:100]), questions=questions)
