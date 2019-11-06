from flask import render_template, request
from app import app
from wordBank import startgame, random_word, answer
#Next Steps: comment everything

@app.route('/', methods=['GET','POST'])
@app.route('/quizpage', methods=['GET', 'POST'])
def quizpage():
    #load wordbank:
    startgame()
    #render quizpage and present user with initial randomized 'term' via random_word function
    if request.method == "GET":
        return render_template('quizPage.html', title='Quiz', term=random_word())
    #user enters answer and clicks "Check" button to initiate POST request
    #create variables from callable form names in quizPage.html so they can be rendered on checkAnswer.html
    if request.method == "POST":
        german_word = request.form['german_word']
        user_answer = request.form['user_answer']
        return render_template('checkAnswer.html', title='Quiz', term=german_word, user_answer=user_answer, correct_answer=answer(german_word, user_answer))
