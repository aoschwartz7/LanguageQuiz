# TODOs:
# -find a way to provide answer without clicking each time
# -add a "Home" button
# -figure out how to center text in quizBox
# -add "Back" button to quizPage

from flask import render_template, request, redirect
from app import app
from quizFunctions import getLanguageFolder, getVocabFiles, startGame, randomTerm, languageSelection, answer, cleanString

# TODO figure out what page homepage should be
@app.route('/', methods=['GET'])
# user can select "GermanToSpanish" on this page, for example

# TODO is this app route even necessary? or should I combine this with above route?
@app.route('/selectLanguage', methods=['GET', 'POST'])
def selectLanguage():
    try:
    # glob for all possible languages within VocabQuiz/Languages
        languageFolder = getLanguageFolder()
        return render_template('selectLanguage.html', languages=languageFolder)
    except:
        return redirect('/')

# show user lesson files within the language they selected
@app.route('/selectLesson', methods=['GET','POST'])
def selectLesson():
    try:
        # (unsure if this makes sense) post language selection to form as languageSelection to remind user of their selection in quizPage.html
        language = request.form['languageFolder']
        # glob for all possible language files
        languageFiles = getVocabFiles(language)
        return render_template('selectLesson.html', lessons=languageFiles, languageSelection=language)
    except:
        return redirect('/')

# load vocab quiz game with lesson selection
@app.route('/loadLesson', methods=['GET', 'POST'])
def lessons():
    try:
        lesson = request.form['lesson']
        lessonFile = startGame(lesson)
        return redirect('/quizPage')
    except:
        return redirect('/')

# generate random vocab term and provide entry form (correct term?) for user to submit an answer
@app.route('/quizPage', methods=['GET', 'POST'])
def quizPage():
    #present user with initial randomized term
    try:
        if request.method == "GET":
            return render_template('quizPage.html', term=randomTerm(), languageSelection = languageSelection())
    except:
        return redirect('/selectLanguage')

    #user enters answer and clicks "Check" button
    #clean their answer by removing articles and punctuation, then assess and show outcome
    if request.method == "POST":
        vocabTerm = request.form['vocabTerm']
        userAnswer = request.form['userAnswer']
        return render_template('checkAnswer.html', \
            term = vocabTerm, \
            userAnswer = cleanString(userAnswer), \
            cleanedAnswer = cleanString(answer(vocabTerm)), \
            fullAnswer = answer(vocabTerm)
        )
