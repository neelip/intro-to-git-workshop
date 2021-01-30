from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'name': '<Name>'}
    questions = [
            'Where are you from?',
            'What programming language do you prefer?'
    ]
    answers = ['Seattle', 'python']
    return render_template('index.html', title='Home', user=user, questions=questions, answers=answers, len=len(questions))
    #return render_template("base.html")