#Next steps:
#1) rename wordBank.py


import json
import random
from datetime import datetime
import glob, os #this is for accessFiles()

# create dict/list instances
wordBank = {}
wordBankKeys = []
wrongWords = {}
newCardSet = {}

# function name: startgame
# parameters: NA
# application: load JSON dictionary as a variable; uses global variables for use across multiple functions;
#              creates list of wordbank keys
# outputs/return values: NA
# this function is called by: routes.py/quizpage, gameTerminal(), reTestWrongWords()
def startGame():
    global wordBank
    global wordBankKeys
    with open('test.json') as jsonFile:
        wordBank = json.load(jsonFile)
    wordBankKeys = list(wordBank.keys())

# function name: getVocabFiles
# application: get names of existing vocabulary files ...
# TODO more comments to match other functions
def getVocabFiles(language):
    fileNames = []
    #change the current working directory to the given path
    os.chdir("/Users/alecschwartz/Desktop/workspace/VocabQuiz/" + language)
    # TODO don't need a loop here...
    # TODO fileNames = glob.glob("*.json")
    for file in glob.glob("*.json"):
        fileNames.append(file)
    return fileNames

# function name: randomWord
# parameters: NA
# application: shuffle wordbank keys and return random word <<-- TODO
# outputs/return values: random german word from wordbank
# function called by: routes.py/quizpage
def randomWord():
    return random.sample(wordBankKeys, 1)[0]

#function name: numRandomWords
#parameters: num
#application: apply randomWord() for particular number of words user chooses to be quizzed on
# TODO ^??
#function called by: gameTerminal()
def numRandomWords(num):
    return random.sample(wordBankKeys, num)


# TODO organize this file, separate funcs used for GUI game and terminal game
# with a barrier e.g.----------------------------


# function name: quizSingleWord
# parameters: vocabTerm, correctAnswer
# application: quizzes user on vocabTerm; compares userAnswer to correctAnswer
# outputs/return values: Boolean T/F
# function called by: gameTerminal(), reTestWrongWords()
def quizSingleWord(vocabTerm, correctAnswer):
    userAnswer = input("What does {} mean in English? ".format(vocabTerm))
    if userAnswer == correctAnswer:
        print("correct! {} means {}".format(vocabTerm, userAnswer))
        return True
    elif userAnswer != correctAnswer:
        print("incorrect. {} means {}".format(vocabTerm, correctAnswer))
        return False

# function name: answer
# parameters: german_word, user_answer
# application: retrieves the correct_answer from wordbank for comparison to user_answer
# outputs/return values: returns right answer
# function is called by: routes.py/quizpage, gameTerminal(), reTestWrongWords()
def answer(vocabTerm):
    correctAnswer = wordBank[vocabTerm]
    return correctAnswer

#function name: createTimeStamp
#parameters: NA
#application: creates timestamp for naming files
#outputs/return values: returns timeStampString
def createTimeStamp():
    timeStamp = datetime.now()
    timeStampString = str(timeStamp.year) + str(timeStamp.month) + str(timeStamp.day) + "_" + str(timeStamp.hour) + "." + str(timeStamp.minute)
    return timeStampString

#function name: createFlashCardSet
#parameters: newTerm, newDefinition
#application: allows user to create a new flashcard set; creates new file; appends new vocab to file.
def createFlashCardSet():
    setName = input("Enter a name for this set: ")
    print("Enter 'done' when finished")
    while True:
        newTerm = input("Enter new term: ")
        if newTerm == "done":
            break
        newDefinition = input("Enter definition for term: ")
        if newDefinition == "done":
            break
        print("adding %s : %s" % (newTerm, newDefinition))
        newCardSet[newTerm] = newDefinition
    cardSetFile = createTimeStamp() + "_" + setName + ".json"
    with open(cardSetFile, "a+") as f:
        json.dump(newCardSet, f)

#function name: openFile
#parameters: NA
#application: prints file names containing wordbanks for quizzes, asks user to select one for quiz, opens that file and begins gameTerminal()
#outputs: NA
def accessFiles():
    #search within directory for file titles that have been timestamped and return them to user
    #ask user to select a file of interest
    #run startGame() with this file
    os.chdir("/Users/alecschwartz/Desktop/workspace/VocabQuiz")
    # TODO don't need loop
    for file in glob.glob("*.json"):
        print(file)
    answer = input("Which flashcard set would you like to open? \n")
    with open(answer) as jsonFile:
        wordBank = json.load(jsonFile)
    wordBankKeys = list(wordBank.keys())

# function name: gameTerminal
# parameters: NA
# application: for local use; retrieves input for userAnswer; compares userAnswer to vocabTerm; creates text file and appends wrong wrongs for re-testing
# outputs/return values: N/A
# function is called by: wordBank.py
def gameTerminal():
    startGame()
    print("Launching quiz...")
    quizWordNum = int(input("How many words would you like to be quizzed on? "))
    miniWordBank = numRandomWords(quizWordNum)
    for i in range(quizWordNum):
        vocabTerm = miniWordBank[i]
        correctAnswer = answer(vocabTerm)
        userIsCorrect = quizSingleWord(vocabTerm, correctAnswer)
        if userIsCorrect == False:
            wrongWords[vocabTerm] = correctAnswer
    wrongWordsFile = createTimeStamp() + ".json"
    with open(wrongWordsFile, "a+") as f:
        json.dump(wrongWords, f)
    reTestWrongWords(wrongWordsFile)

# function name: reTestWrongWords
# parameters: NA
# application: run startGame(); open wrongWords text file; user quizSingleWord() to iterate through word bank
# outputs/return values: N/A
# function is called by: wordBank.py
def reTestWrongWords(fileName):
    reQuiz = input("Would you like to be quizzed on the words you missed? Y/N ")
    if reQuiz in ["Y", "y", "YES", "yes", "yas"]:
        with open(fileName) as wrongWordsJson:
            wordBank = json.load(wrongWordsJson)
        for i in wordBank:
            vocabTerm = i
            correctAnswer = answer(vocabTerm)
            quizSingleWord(vocabTerm, correctAnswer)
    else:
        print("Good work! See you next time. ")
        quit()

# TODO comment here to say when this code would run 
if __name__=="__main__":
    createFlashCardSet()
    accessFiles()
    gameTerminal()
