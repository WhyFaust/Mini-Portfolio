from random import randint
from flask import Flask, redirect, url_for
from db_scripts import get_question_after

app = Flask(__name__)

quiz = 0
last_question = 0

@app.route('/')
def index():
    global quiz, last_question
    max_quiz = 3
    quiz = randint(1, max_quiz)
    last_question = 0
    return '<a href="/test">Тест</a>'

@app.route('/test')
def test():
    global last_question
    result = get_question_after(last_question, quiz)
    if result is None or len(result) == 0:
        return redirect(url_for('result'))
    last_question = result[0]
    return f"<h1>{quiz}<br>{result}</h1>"

@app.route('/result')
def result():
    return "that's all folks!"

if __name__ == '__main__':
    app.run()