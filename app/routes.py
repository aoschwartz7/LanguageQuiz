# TODOs:
# -
# -

from flask import render_template, request
from app import app
from wordBank import startGame, randomWord, answer, getVocabFiles

# TODO figure out what page homepage should be
@app.route('/', methods=['GET','POST'])

# TODO comment here too -- overview of welcomePage
@app.route('/welcomePage', methods=['GET', 'POST'])
def selectLanguage():
    if request.method == 'GET':
        # TODO glob for all possible languages, pass list in to selectLanguage.html
        return render_template('selectLanguage.html')

    #capture user's selection of German or Spanish (or other language)
    if request.method == 'POST':
        language = request.form['language']
        languageFiles = getVocabFiles(language)
        return render_template('lessons.html', lessons=languageFiles)

# TODO comment here too
@app.route('/lessons', methods=['GET', 'POST'])
def dropdown():
    return render_template('lessons.html')

# TODO comment here too
@app.route('/quizPage', methods=['GET', 'POST'])
def quizPage():
    # TODO load selected wordbank
    # TODO need argument to startGame
    # TODO do we want to call startGame for every word?
    startGame()
    #render quizpage and present user with initial randomized 'term' via random_word()
    if request.method == "GET":
        return render_template('quizPage.html', title='Quiz', term=randomWord())
    #user enters answer and clicks "Check" button to initiate POST request
    #create variables from callable form input names in quizPage.html so they can be rendered on checkAnswer.html
    if request.method == "POST":
        vocabTerm = request.form['vocabTerm']
        userAnswer = request.form['userAnswer']
        return render_template('checkAnswer.html', title='Quiz', term=vocabTerm, userAnswer=userAnswer, correctAnswer=answer(vocabTerm))
