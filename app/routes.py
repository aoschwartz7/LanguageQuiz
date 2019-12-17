# TODOs:
# -consider using a base.html template and the extends method to create a consistent layout (see chp2 Grinberg blog)
# -consider using action attribute of <form> in some cases (chp2 Grinberg)

from flask import render_template, request, redirect
from app import app
from wordBank import startGame, randomWord, answer, getVocabFiles

# TODO figure out what page homepage should be
@app.route('/', methods=['GET','POST'])

# TODO comment here too -- overview of welcomePage
@app.route('/selectLanguage', methods=['GET', 'POST'])
def selectLanguage():
    # TODO glob for all possible languages, pass list in to selectLanguage.html
    return render_template('selectLanguage.html')


#NEW
@app.route('/selectLesson', methods=['GET','POST'])
def selectLesson():
    #capture user's selection of German or Spanish (or other language)
    language = request.form['language']
    languageFiles = getVocabFiles(language)
    return render_template('lessons.html', lessons=languageFiles)


# TODO comment here too
@app.route('/loadLesson', methods=['GET', 'POST'])
def lessons():
    lesson = request.form['fileName']
    lessonFile = startGame(lesson)
    return redirect('/quizPage')


# TODO comment here too
@app.route('/quizPage', methods=['GET', 'POST'])
def quizPage():
    #render quizpage and present user with initial randomized 'term' via random_word()
    if request.method == "GET":
        return render_template('quizPage.html', term=randomWord())

    #user enters answer and clicks "Check" button to initiate POST request
    #create variables from callable form input names in quizPage.html so they can be rendered on checkAnswer.html
    if request.method == "POST":
        vocabTerm = request.form['vocabTerm']
        userAnswer = request.form['userAnswer']
        return render_template('checkAnswer.html', \
            term=vocabTerm, userAnswer=userAnswer, correctAnswer=answer(vocabTerm))
