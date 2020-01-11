# TODOs:
# -find a way to provide answer without clicking each time
# -add a "Home" button

from flask import render_template, request, redirect
from app import app
from wordBank import startGame, randomWord, answer, getLanguageFolder, getVocabFiles, languageSelection, cleanString

# TODO figure out what page homepage should be
@app.route('/', methods=['GET'])

# TODO comment here too -- overview of welcomePage
@app.route('/selectLanguage', methods=['GET', 'POST'])
def selectLanguage():
    # TODO glob for all possible languages, pass list into selectLanguage.html
    try:
        #show user language folders
        languageFolders = getLanguageFolder()
        return render_template('selectLanguage.html', languages=languageFolders)
    except:
        return redirect('/')

@app.route('/selectLesson', methods=['GET','POST'])
def selectLesson():
    try:
        #capture user's selection of German or Spanish (or other language)
        language = request.form['languageFolder']
        languageFiles = getVocabFiles(language)
        return render_template('selectLesson.html', lessons=languageFiles, languageSelection=language)
    except:
        return redirect('/')

# TODO comment here too
@app.route('/loadLesson', methods=['GET', 'POST'])
def lessons():
    try:
        lesson = request.form['fileName']
        lessonFile = startGame(lesson)
        return redirect('/quizPage')
    except:
        return redirect('/')

# TODO comment here too
@app.route('/quizPage', methods=['GET', 'POST'])
def quizPage():
    #render quizpage and present user with initial randomized 'term' via random_word()
    try:
        if request.method == "GET":
            return render_template('quizPage.html', term=randomWord(), languageSelection = languageSelection())
    except:
        return redirect('/selectLanguage')

    #user enters answer and clicks "Check" button
    if request.method == "POST":
        vocabTerm = request.form['vocabTerm']
        userAnswer = request.form['userAnswer']
        return render_template('checkAnswer.html', \
            term=vocabTerm, userAnswer=userAnswer, correctAnswer=answer(vocabTerm), \
            outcome=(cleanString(userAnswer)==cleanString((answer(vocabTerm)))))
