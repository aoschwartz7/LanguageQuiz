from flask import render_template
from app import app
from wordBank import startgame, random_word

@app.route('/')
@app.route('/quizpage')
def quizpage():
    startgame()
    return render_template('quizPage.html', title='Quiz', term= random_word())
