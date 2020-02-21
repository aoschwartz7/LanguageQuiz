# There are two sections to this file:
# Section 1) Python-Flask App Functions: contains functions for Python-Flask app.
# Section 2) Local-use Functions: builds off Section 1 to allow for app's local \
#            use with Terminal.
# ------------------------------------------------------------------------------
import json
import random
import time
from datetime import datetime
import glob, os
# ------------------------------------------------------------------------------
# Section 1) Python-Flask App Functions
# ------------------------------------------------------------------------------

# create dictionary and list instances
wordBank = {}
wordBankKeys = []
newCardDeck = {}
cardDeckSelection = ""

# function name: startGame()
# parameters: lessonFile
# application: load JSON dictionary from lessonFile as the global variable wordBank;
#              create list of wordBank keys so randomWord() can randomize terms
# output: NA
# called by: routes.py/loadLesson, Section 2)
def startGame(lessonFile):
    global wordBank
    global wordBankKeys
    with open(lessonFile + '.json') as jsonFile:
        wordBank = json.load(jsonFile)
    wordBankKeys = list(wordBank.keys())

# function name: getCardDeckFolders()
# parameters: NA
# application: open VocabQuiz/Languages pathway and return folder contents \
#             (ie GermanToSpanish, GermantoEnglish, etc)
# output: folderNames within VocabQuiz/Languages pathway
# called by: routes.py/selectLanguage, Section 2)
# TODO: figure out how to reduce pathway
def getCardDeckFolders():
    #change the current working directory to path containing card deck folders
    os.chdir("./FlashcardDeckFolders")
    folderNames = glob.glob("*")
    return folderNames

# function name: createCardDeckFolder()
# parameters: folderName
# application: create new flashcard deck directory for user
# output:
# called by:
# TODO: figure out how to reduce pathway
def createCardDeckFolder(folderName):
    os.mkdir(folderName)
    # os.mkdir("/Users/alecschwartz/Desktop/workspace/VocabQuiz/FlashcardDeckFolders/" +
    # folderName)

# function name: fillCardDeck()
# parameters: newTerm, new Definition
# application: create new flashcard deck
# output: NA
# called by: routes.py/createCardDeck
def fillCardDeck(newTerm, newDefinition):
    # call global variable newCardDeck{} so we can add flashcards to it
    global newCardDeck
    newCardDeck[newTerm] = newDefinition

# function name: emptyCardDeck()
# parameters: NA
# application: empty newCardDeck once user finishes creating the card deck
# output: emptied newCardDeck
# called by: routes.py/createCardDeck
def emptyCardDeck():
    global newCardDeck
    newCardDeck = {}

# function name: createCardDeck()
# parameters: deckTitle
# application: create new JSON file named after user-assigned title
#              and append newCardDeck to file
# output: NA
# called by: routes.py/createCardDeck
def createCardDeck(deckTitle):
    global newCardDeck
    fileName = deckTitle + ".json"
    with open(fileName, "a+") as file:
        json.dump(newCardDeck, file)


# function name: getCardDeckFiles()
# parameters: userSelection
# application: retrieve existing .json fileNames that contain vocab dictionaries \
#              when user selects a language in routes.py/loadLesson
# output: fileNames
# called by: routes.py/selectLesson
def getCardDeckFiles(deckFolder):
    # change the current working directory to the given path
    os.chdir("./" + deckFolder )
    fileNames = glob.glob("*.json")
    fileNames = [filename.split(".")[0] for filename in fileNames]
    return fileNames

# function name: cardDeckSelection()
# parameters: NA
# application: this is a helper function that can be used to return the value of \
#              the global variable cardDeckSelection
# outputs: cardDeckSelection
# called by: routes.py/quizPage
# def cardDeckSelection():
#     return cardDeckSelection

# function name: randomTerm()
# parameters: NA
# application: return a random term from the global variable wordBankKeys
# outputs/return values: random term
# function called by: routes.py/quizPage
def randomTerm():
    return random.sample(wordBankKeys, 1)[0]

# function name: answer()
# parameters: vocabTerm
# application: uses the wordBank dictionary key-value pairing to show the \
#              correctAnswer (value) for the current vocabTerm (key)
# outputs: correctAnswer
# function called by: routes.py/quizPage
def answer(vocabTerm):
    correctAnswer = wordBank[vocabTerm]
    return correctAnswer

# function name: cleanString()
# parameters: stringToClean
# application: strips away articles from both userAnswer and correctAnswer \
#              to make user's response more flexible
# output: stringToClean
# function called by: routes.py/quizPage
def cleanString(stringToClean):
    #extraneous stuff to remove
    articles = ["the ","an ", "a ", "el ", "la ", "to"]
    punctuation = [".", ",", ":", ";", "?"]
    stringToClean = stringToClean.lower()
    #if term is "el niño/la niña" ie, split by "/" first
    stringToClean.split("/")
    stringToClean.split(' ')
    #remove articles and punctuation
    for x in articles:
        stringToClean = stringToClean.replace(x, "")
    for x in punctuation:
        stringToClean = stringToClean.replace(x, " ")
    stringToClean = ' '.join(stringToClean)
    #remove whitespace
    stringToClean = stringToClean.strip()
    return stringToClean
# ------------------------------------------------------------------------------
# Section 2) Local-use Functions: builds off Section 1 to allow for app's local \
#            use with Terminal.
# ------------------------------------------------------------------------------
# function name: quizTerm()
# parameters: vocabTerm
# application: quizzes user on vocabTerm and compares userAnswer to correctAnswer
# outputs: Boolean T/F
# function called by: gameTerminal(), reTestWrongWords()
def quizTerm(vocabTerm):
    userAnswer = input("What does {} mean? ".format(vocabTerm))
    cleanedResponse = stringToClean(userAnswer)
    cleanedAnswer = stringToClean(answer(vocabTerm))
    if cleanedResponse == cleanedAnswer:
        print("correct! {} means {}".format(vocabTerm, answer(vocabTerm)))
        return True
    elif cleanedResponse != corrcleanedAnswerectAnswer:
        print("incorrect. {} means {}".format(vocabTerm, answer(vocabTerm)))
        return False

# function name: createTimeStamp()
# parameters: NA
# application: creates a timeStampString for naming flashcard sets created \
#              using createFlashCardSet()
# output: timeStampString
# function called by: createFlashCardSet()

def createTimeStamp():
    timeStamp = datetime.now()
    timeStampString = str(timeStamp.year) + str(timeStamp.month) \
    + str(timeStamp.day)
    return timeStampString

# function name: createFlashCardSet()
# parameters: NA
# application: allows user to create a new flashcard set as a JSON file
# output: NA
# function called by: __main__
def createFlashCardSet():
    #prompt user to create new flashcard set if they would like to
    while True:
        makeSet = input("Would you like to create a new flashcard set? (y/n) ")
        if makeSet == 'n':
            return
        if makeSet == 'y':
            break
        else:
            print("enter 'y' or 'n' ")

    #prompt user for title

    setTitle = input("Enter a title for this flashcard set: ")
    print("Enter 'done' when finished")
    #prompt user for new vocab
    while True:
        newTerm = input("Enter new term: ")
        if newTerm == "done":
            break
        newDefinition = input("Enter definition for term: ")
        if newDefinition == "done":
            break
        #add term and definition to newCardDeck{}
        print("adding %s : %s\n" % (newTerm, newDefinition))
        newCardDeck[newTerm] = newDefinition
    #create timestamped JSON file for new set
    cardSetFile = createTimeStamp() + "_" + setTitle + ".json"
    with open(cardSetFile, "a+") as file:
        json.dump(newCardDeck, file)

# function name: accessFiles()
# parameters: NA
# application: prints flashcard set file names, asks user to select one \
#              for the quiz, opens that file and launches the game
# output: NA
# function is called by: __main__
def accessFiles():
    #search within directory for JSON files
    os.chdir("./VocabQuiz")
    # TODO don't need loop
    for file in glob.glob("*.json"):
        time.sleep(.5)
        print(file)
    time.sleep(2)
    print("Which flashcard set would you like to open?")
    time.sleep(2)
    fileSelection = input("Type out the entire name of the file and then press \
'Enter': ")
    return fileSelection

# function name: gameTerminal()
# parameters: NA
# application: runs startGame() to select vocab file and initialize wordBank;\
#              compares userAnswer to correctAnswer; \
#              creates new JSON file and appends wrong wrongs for re-testing later
# output: N/A
# function is called by: "__main__"

def gameTerminal():
    print("Here is a list of the flashcard sets stored in your VocabQuiz folder:")
    time.sleep(2)
    #show user all JSON files contained in current directory
    accessFiles()
    time.sleep(.5)
    #run startGame() with user's fileSelection
    print("Launching quiz...")
    time.sleep(3)
    startGame(fileSelection)
    #loop through terms in JSON file selecton
    for i in range(fileSelection):
        quizTerm()
    print("That's the entire vocab set. Program will now quit. ")
    quit()


# TODO comment here to say when this code would run
if __name__=="__main__":
    accessFiles()
    # print("----------------------------------------------------")
    # print("Welcome to the Language Learner's Vocabulary Quiz!")
    # time.sleep(2)
    # createFlashCardSet()
    # gameTerminal()
