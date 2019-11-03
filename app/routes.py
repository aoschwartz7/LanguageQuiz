from flask import render_template, request
from app import app
from wordBank import startgame, random_word, answer
#Next steps: create new template for right or wrong answer

@app.route('/', methods=['GET','POST'])
@app.route('/quizpage', methods=['GET', 'POST'])
def quizpage():
    #load wordbank & shuffle terms:
    startgame()
    #render quizpage and present user with initial randomized 'term':
    if request.method == "GET":
        return render_template('quizPage.html', title='Quiz', term=random_word())
    #user enters answer and clicks "Check" button:
    if request.method == "POST":
        german_word = request.form['german_word']
        user_answer = request.form['user_answer']
        return render_template('checkAnswer.html', title='Quiz', term=german_word, user_answer=user_answer, correct_answer=answer(german_word, user_answer))
