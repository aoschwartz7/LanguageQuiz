from flask import render_template, request
from app import app
from wordBank import startGame, randomWord, answer

@app.route('/', methods=['GET','POST'])
@app.route('/quizPage', methods=['GET', 'POST'])
def quizPage():
    #load wordbank:
    startGame()
    #render quizpage and present user with initial randomized 'term' via random_word function
    if request.method == "GET":
        return render_template('quizPage.html', title='Quiz', term=randomWord())
    #user enters answer and clicks "Check" button to initiate POST request
    #create variables from callable form names in quizPage.html so they can be rendered on checkAnswer.html
    if request.method == "POST":
        germanWord = request.form['germanWord']
        userAnswer = request.form['userAnswer']
        return render_template('checkAnswer.html', title='Quiz', term=germanWord, userAnswer=userAnswer, correctAnswer=answer(germanWord))
