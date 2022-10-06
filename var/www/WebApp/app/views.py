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


@app.route('/')
def home():
    return "<b>There has been a change!!!!!!@@@@@</b>"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/template')
def template():
    return render_template('home.html')

@app.route('/karimen')
def karimen():
    questions = []

    try:
        with open('app/Question.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                questions.append(Ques(row[1], row[4]))

            random.shuffle(questions)
    except Exception as error:
        return str(error)

    return render_template('karimen.html', len=len(questions[:50]), questions=questions)
