from random import randint
from flask import Flask, session, redirect, url_for
from db_scripts import get_question_after

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretLife'

@app.route('/')
def index():
    max_quiz = 3
    session['quiz'] = randint(1, max_quiz)
    session['last_question'] = 0
    return '<a href="/test">Тест</a>'

@app.route('/test')
def test():
    result = get_question_after(session['last_question'], session['quiz'])
    if result is None or len(result) == 0:
        return redirect(url_for('result'))
    session['last_question'] = result[0]
    return f"<h1>{session['quiz']}<br>{result}</h1>"

@app.route('/result')
def result():
    return "that's all folks!"

if __name__ == '__main__':
    app.run()