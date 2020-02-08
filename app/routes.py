# TODOs:
# -find a way to provide answer without clicking each time
# -add a "Home" button
# -figure out how to center text in quizBox
# -add "Back" button to quizPage
# -allow user to create new flashcard sets from homepage

from flask import render_template, flash, request, redirect
from app import app
from quizFunctions import getCardDeckFolders, createCardDeckFolder, \
getCardDeckFiles, fillCardDeck, createCardDeck, startGame, randomTerm, \
cardDeckSelection, answer, cleanString

# TODO figure out what page homepage should be
@app.route('/', methods=['GET'])
# user can choose to create a new flashcard set or continue to quiz using \
# existing files
@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    if request.method == "GET":
        return render_template('homepage.html')
    #user chooses to continue to quiz
    if request.method =="POST":
        return render_template('quizCardDeckFolders.html')
# user can select an existing flashcard deck folder for their new deck
# or create a new flashcard deck folder
@app.route('/selectCardDeckFolder', methods=['GET', 'POST'])
def newCardDeck():
    if request.method == "GET":
        cardDeckFolders = getCardDeckFolders()
        return render_template('selectCardDeckFolder.html',
            folders=cardDeckFolders
        )
    if request.method == "POST":
        try:
            #if user decides to create new card deck folder, add their new folder to
            #VocabQuiz/FlashcardDeckFolders
            newFolder = request.form['newCardDeckFolder']
            newFolder = createCardDeckFolder(newFolder)
            #flash message that folder was created
            # flash("New folder created! Select it below.")
            return render_template('selectCardDeckFolder.html',
                folders=getCardDeckFolders()
            )
        except:
            return redirect('/')
# user can select language here
# TODO is this app route even necessary? or should I combine this with above route?
@app.route('/createCardDeck', methods=['GET', 'POST'])
def createCardDeck():
    if request.method == "POST":
        try:
            # first if statement is triggered when user switches between
            #/selectCardDeckFolder to /createCardDeck
            if 'cardDeckFolders' in request.form:
                cardDeckFolder = request.form['cardDeckFolders']
                return render_template('createCardDeck.html',
                    folderName=cardDeckFolder
                )
            #once user finishes deck, titles it, and clicks "done":
            if 'newCardDeckTitle' in request.form:
                newDeckTitle = request.form['newCardDeckTitle']
                folderName=request.form['folderName']
                return render_template('homepage.html',
                folderName=folderName,
                makeJSONFile=createCardDeck(newDeckTitle)
                )
            else:
                newTerm = request.form['newTerm']
                newDefinition = request.form['newDefinition']
                folderName = request.form['folderName']
                return render_template('createCardDeck.html',
                    fillCardDeck=fillCardDeck(newTerm, newDefinition),
                    folderName=folderName
                    )
        except:
            return redirect('/')
# if user selects "Continue to Quiz" on /homepage, direct user here
@app.route('/quizCardDeckFolders', methods=['POST'])
def quizCardDeckFolders():
    try:
        # glob for all possible flashcard folders
        cardDeckFolders = getCardDeckFolders()
        return render_template('quizCardDeckFolders.html',
        folders=cardDeckFolders
        )
    except:
        return redirect('/')
@app.route('/quizCardDeck', methods=['POST'])
def quizCardDeck():
    try:
        deckFolder = request.form['cardDeckFolders']
        #retrieve user's 'folder' selection from form and return files from it
        return render_template('quizCardDeck.html',
        files = getCardDeckFiles(deckFolder)
        )
    except:
        return redirect('/')
# load quiz via startGame() and redirect user to quizPage.html
@app.route('/loadQuiz')
def loadQuiz():
    flashcardFile = request.form['cardDecks']
    startGame(flashcardFile)
    return redirect('quizPage.html')
# show user randomized term and allow them to enter answer
@app.route('/quizPage', methods=['POST'])
def quizPage():
    #present user with initial randomized term if request.method == "GET":
    if request.method == "GET":
        return render_template('quizPage.html', term=randomTerm())
    #user enters answer and clicks "Check" button;
    #clean their answer by removing articles/punctuation then show outcome
    if request.method == "POST":
        vocabTerm = request.form['vocabTerm']
        userAnswer = request.form['userAnswer']
        return render_template('checkAnswer.html', \
            term = vocabTerm, \
            userAnswer = cleanString(userAnswer), \
            cleanedAnswer = cleanString(answer(vocabTerm)), \
            fullAnswer = answer(vocabTerm)
        )
