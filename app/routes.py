# TODOs:
# -consider using a base.html template and the extends method to create a consistent layout (see chp2 Grinberg blog)
# -create GUI that displays results (correct/wrong) and streaks (with dancing monkeys)
# -find a way to provide answer without clicking each time
# -create a route to redirect user back to lesson or language selection

from flask import render_template, request, redirect
from app import app
from wordBank import startGame, randomWord, answer, getVocabFiles

# TODO figure out what page homepage should be
@app.route('/', methods=['GET'])

# TODO comment here too -- overview of welcomePage
@app.route('/selectLanguage', methods=['GET', 'POST'])
def selectLanguage():
    # TODO glob for all possible languages, pass list into selectLanguage.html
    return render_template('selectLanguage.html')

@app.route('/selectLesson', methods=['GET','POST'])
def selectLesson():
    #capture user's selection of German or Spanish (or other language)
    language = request.form['language']
    languageFiles = getVocabFiles(language)
    return render_template('selectLesson.html', lessons=languageFiles)

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

    #user enters answer and clicks "Check" button
    if request.method == "POST":
        vocabTerm = request.form['vocabTerm']
        userAnswer = request.form['userAnswer']
        return render_template('checkAnswer.html', \
            term=vocabTerm, userAnswer=userAnswer, correctAnswer=answer(vocabTerm))
