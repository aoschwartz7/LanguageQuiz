from flask import render_template, flash, request, redirect
from app import app
import os
from quizFunctions import getCardDeckFolders, createCardDeckFolder, \
getCardDeckFiles, fillCardDeck, emptyCardDeck, createCardDeck, startGame, \
randomTerm, cardDeckSelection, answer, cleanString


@app.route('/', methods=['GET'])

@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    if request.method == "GET":
        return render_template('homepage.html')

# User can select an existing flashcard deck folder for their new deck
#   or create a new flashcard deck folder.
@app.route('/selectCardDeckFolder', methods=['GET', 'POST'])
def newCardDeck():
    if request.method == "GET":
        # TODO: fix this pathway
        os.chdir("/Users/alecschwartz/Desktop/workspace/VocabQuiz")
        # Retrieve folders containing flashcard decks.
        cardDeckFolders = getCardDeckFolders()
        return render_template('selectCardDeckFolder.html',
            folders=cardDeckFolders
            )
# If user decides to create a new folder, add their new folder to
#   VocabQuiz/FlashcardDeckFolders
    if request.method == "POST":
        try:
            newFolder = request.form['newCardDeckFolder']
            # Create new folder.
            newFolder = createCardDeckFolder(newFolder)
            os.chdir("..")
            return render_template('selectCardDeckFolder.html',
                folders=getCardDeckFolders()
                )
        except:
            return redirect('/')

# User has selected a folder for their new deck and can now create cards.
@app.route('/createCardDeck', methods=['GET', 'POST'])
def createCardDeckProcess():
    if request.method == "POST":
        try:
            # First if statement is triggered when user switches between
            # /selectCardDeckFolder to /createCardDeck.
            if 'cardDeckFolders' in request.form:
                cardDeckFolder = request.form['cardDeckFolders']
                return render_template('createCardDeck.html',
                    folderName=cardDeckFolder
                    )
            # Once user finishes adding cards, titles the deck, and clicks
            #   "done":
            if 'newCardDeckTitle' in request.form:
                newDeckTitle = request.form['newCardDeckTitle']
                folderName = request.form['folderName']
                os.chdir("./" + folderName)
                createCardDeck(newDeckTitle)
                emptyCardDeck()
                os.chdir("..")
                return render_template('homepage.html',
                    folderName=folderName
                    )
            # Allow user to add new cards to deck.
            else:
                newTerm = request.form['newTerm']
                newDefinition = request.form['newDefinition']
                folderName = request.form['folderName']
                fillCardDeck(newTerm, newDefinition)
                return render_template('createCardDeck.html',
                    folderName=folderName
                    )
        except:
            return redirect('/')


# When user selects "Continue to Quiz" on /homepage, have them select a folder.
@app.route('/quizCardDeckFolders', methods=['POST'])
def quizCardDeckFolders():
    try:
        # Glob for all possible flashcard folders.
        cardDeckFolders = getCardDeckFolders()
        return render_template('quizCardDeckFolders.html',
            folders=cardDeckFolders
            )
    # Fix the pathway to the correct directory.
    except:
        # TODO: configure path
        os.chdir("/Users/alecschwartz/Desktop/workspace/VocabQuiz")
        cardDeckFolders = getCardDeckFolders()
        return render_template('quizCardDeckFolders.html',
            folders=cardDeckFolders
            )

# After user picks a folder, show them existing flashcard decks for selection.
@app.route('/quizCardDeck', methods=['POST'])
def quizCardDeck():
    try:
        deckFolder = request.form['cardDeckFolders']
        return render_template('quizCardDeck.html',
            files = getCardDeckFiles(deckFolder)
            )
    except:
        return redirect('/')


# Load quiz via startGame() and redirect user to quizPage.html.
@app.route('/loadQuiz', methods=['POST'])
def loadQuiz():
    flashcardFile = request.form['cardDecks']
    startGame(flashcardFile)
    return redirect('quizPage')


# Show user randomized term and have them enter an answer.
@app.route('/quizPage', methods=['GET','POST'])
def quizPage():
    # Present user with a random flashcard.
    if request.method == "GET":
        return render_template('quizPage.html',
            term=randomTerm()
            )
    # User enters an answer and clicks "Check" button. Remove articles and
    #   punctuation from their answer so it's more flexibile then show them
    #   the outcome.
    if request.method == "POST":
        vocabTerm = request.form['vocabTerm']
        userAnswer = request.form['userAnswer']
        return render_template('checkAnswer.html',
            term = vocabTerm,
            fullAnswer = answer(vocabTerm),
            outcome = (cleanString(userAnswer)==cleanString(answer(vocabTerm)))
            )
