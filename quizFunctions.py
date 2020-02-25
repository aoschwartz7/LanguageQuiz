# There are two sections to this file:
# Section 1) Python-Flask content: contains functions for Python-Flask app so the
#               app can run on local 5000.
# Section 2) Terminal-use content: builds off Section 1 to allow for app's use
#                with Terminal.
# ------------------------------------------------------------------------------
import json
import random
import time
import glob, os
# ------------------------------------------------------------------------------
# Section 1) Python-Flask content
# ------------------------------------------------------------------------------

# Create dictionary and list instances for creating new flashcards and
#     loading pre-existing flashcards.
wordBank = {}
wordBankKeys = []
newCardDeck = {}
cardDeckSelection = ""


# function name: startGame()
# parameters: lessonFile
# application:     Load JSON dictionary content (flashcards) from lessonFile as
#                  the global variable wordBank; create list of wordBank keys
#                  so randomWord() can randomize terms.
# output: NA
# called by: routes.py/loadLesson, Section 2) gameTerminal()
def startGame(lessonFile):
    global wordBank
    global wordBankKeys
    with open(lessonFile + '.json') as jsonFile:
        wordBank = json.load(jsonFile)
    wordBankKeys = list(wordBank.keys())


# function name: getCardDeckFolders()
# parameters: NA
# application:      Navigate pathway to VocabQuiz/FlashcardDeckFolders where
#                   folders containing flashcard sets are located.
# output: folderNames
# called by: routes.py/selectCardDeckFolder, routes.py/quizCardDeckFolders
def getCardDeckFolders():
    # Change the current working directory.
    os.chdir("./FlashcardDeckFolders")
    folderNames = glob.glob("*")
    return folderNames


# function name: createCardDeckFolder()
# parameters: folderName
# application:    Create new flashcard deck directory in
#                 VocabQuiz/FlashcardDeckFolders for user.
# output: NA
# called by: routes.py/selectCardDeckFolder
def createCardDeckFolder(folderName):
    os.mkdir(folderName)


# function name: fillCardDeck()
# parameters: newTerm, newDefinition
# application:    Create new flashcard deck.
# output: NA
# called by: routes.py/createCardDeck, Section 2) createFlashcardSet()
def fillCardDeck(newTerm, newDefinition):
    # Call global variable newCardDeck{} so we can add flashcards to it.
    global newCardDeck
    newCardDeck[newTerm] = newDefinition


# function name: emptyCardDeck()
# parameters: NA
# application:    Empty newCardDeck once user finishes making it.
# output: NA
# called by: routes.py/createCardDeck
def emptyCardDeck():
    global newCardDeck
    newCardDeck = {}


# function name: createCardDeck()
# parameters: deckTitle
# application:    Create new JSON file named after user-assigned title
#                 and append newCardDeck to file.
# output: NA
# called by: routes.py/createCardDeck
def createCardDeck(deckTitle):
    global newCardDeck
    fileName = deckTitle + ".json"
    with open(fileName, "a+") as file:
        json.dump(newCardDeck, file)


# function name: getCardDeckFiles()
# parameters: deckFolder
# application: Retrieve existing .json fileNames that contain flashcards.
# output: fileNames
# called by: routes.py/quizCardDeck, Section 2) showCardDecks()
def getCardDeckFiles(deckFolder):
    # Change the current working directory to the given path.
    os.chdir("./" + deckFolder )
    fileNames = glob.glob("*.json")
    fileNames = [filename.split(".")[0] for filename in fileNames]
    return fileNames


# function name: randomTerm()
# parameters: NA
# application:    Return a random term from the global variable wordBankKeys.
# output: random term
# function called by: routes.py/quizPage, Section 2) quizTerm()
def randomTerm():
    return random.sample(wordBankKeys, 1)[0]

# function name: answer()
# parameters: vocabTerm
# application:    Return vocabTerm's correctAnswer from wordBank.
# output: correctAnswer
# function called by: routes.py/quizPage, Section 2) quizTerm()
def answer(vocabTerm):
    correctAnswer = wordBank[vocabTerm]
    return correctAnswer

# function name: cleanString()
# parameters: stringToClean
# application:    Strips away articles and punctuation from both userAnswer and
#                 correctAnswer to make user's response more flexible.
# output: stringToClean
# function called by: routes.py/quizPage, Section 2) quizTerm()
def cleanString(stringToClean):
    # Extraneous stuff to remove:
    articles = ["the ","an ", "a ", "el ", "la ", "to"]
    punctuation = [".", ",", ":", ";", "?"]
    stringToClean = stringToClean.lower()
    # If term is "el niño/la niña" ie, split by "/" first.
    stringToClean.split("/")
    stringToClean.split(' ')
    # Remove articles and punctuation.
    for x in articles:
        stringToClean = stringToClean.replace(x, "")
    for x in punctuation:
        stringToClean = stringToClean.replace(x, " ")
    stringToClean = ''.join(stringToClean)
    # Remove whitespace.
    stringToClean = stringToClean.strip()
    return stringToClean
# ------------------------------------------------------------------------------

# Section 2) Terminal-use content: builds off Section 1 to allow for app's use
#                with Terminal.

# ------------------------------------------------------------------------------
# function name: quizTerm()
# parameters: vocabTerm
# application:    Quizzes user on vocabTerm and compares userAnswer to correctAnswer.
# outputs: Boolean T/F
# function called by: gameTerminal()
def quizTerm():
    term = randomTerm()
    time.sleep(1)
    # Quiz user with flashcard.
    userAnswer = input("What does {} mean? ".format(term))
    userAnswer = cleanString(userAnswer)
    correctAnswer = cleanString(answer(term))
    time.sleep(1)
    # See if they're correct.
    if userAnswer == correctAnswer:
        print("correct! {} means {} \n".format(term, answer(term)))
        return True
    # In gameTerminal(), 'done' will break While loop.
    elif userAnswer == 'done':
        return False
    elif userAnswer != correctAnswer:
        print("incorrect. {} means {} \n".format(term, answer(term)))
        return True


# function name: createFlashcardSet()
# parameters: NA
# application:    Allows user to create a new flashcard set (ie JSON file).
# output: NA
# function called by: __main__
def createFlashcardSet():
    # Prompt user to create new flashcard set if they would like to.
    while True:
        makeSet = input("Would you like to create a new flashcard set? (y/n) ")
        if makeSet == 'n':
            return
        if makeSet == 'y':
            break
        else:
            print("enter 'y' or 'n' ")
    time.sleep(1)
    # Prompt user for new cards.
    print("Enter 'done' when finished.\n")
    while True:
        time.sleep(1)
        newTerm = input("Enter new term: ")
        if newTerm == "done":
            break
        newDefinition = input("Enter definition for term: ")
        if newDefinition == "done":
            break
        print("adding %s : %s\n" % (newTerm, newDefinition))
        # Add new card to deck.
        fillCardDeck(newTerm, newDefinition)
    # Change path to folder containing flashcards.
    os.chdir('./TerminalFlashcards')
    setTitle = input("\nEnter a title for this flashcard set: ")
    # Add new flashcard deck to folder.
    createCardDeck(setTitle)
    # Navigate back to /VocabQuiz.
    os.chdir('..')


# function name: showCardDecks()
# parameters: TerminalFlashcards
# application:    Prints flashcard set file names.
# output: NA
# function is called by: __main__
def showCardDecks(TerminalFlashcards):
    fileList = getCardDeckFiles(TerminalFlashcards)
    for fileName in fileList:
        print(fileName)
        time.sleep(0.2)


# function name: gameTerminal()
# parameters: NA
# application:    Show user available card decks for the quiz, have them select
#                 a deck, then start the quiz with that file.
# output: N/A
# function is called by: __main__

def gameTerminal():
    print("Here are your available flashcard sets: \n")
    time.sleep(.5)
    #show user all JSON files stored in /TerminalFlashcards
    showCardDecks("TerminalFlashcards")
    time.sleep(1)
    file = input("\nSelect a set for the quiz by entering its full name as shown\
 above, then hit 'Enter': \n")
    startGame(file)
    time.sleep(.5)
    print("\nTo end the quiz, enter 'done'.\n")
    time.sleep(.5)
    keepPlaying = True
    # If user enters 'done' in quizTerm(), False gets triggered to break While loop.
    while keepPlaying:
        keepPlaying = quizTerm()
    time.sleep(.5)
    print("\nThanks for playing!")

# __main__ runs when the user runs quizFunctions.py in Terminal.

if __name__=="__main__":
    time.sleep(.5)
    print("\nWelcome to the Language Learner's Vocab Quiz!\n")
    time.sleep(.5)
    createFlashcardSet()
    time.sleep(.5)
    gameTerminal()
    time.sleep(1)
