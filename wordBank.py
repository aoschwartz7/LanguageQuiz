#Next steps:
# -rename wordBank.py
# -work on approximateAnswer()


import json
import random
from datetime import datetime
import glob, os

# create dict/list instances
wordBank = {}
wordBankKeys = []
wrongWords = {}
newCardSet = {}

# function name: startGame()
# parameters: lessonFile
# application: load JSON dictionary from the file lessonFile as a variable;
# creates list of wordBank keys for quiz randomization via randomWord()
# outputs/return values: NA
# called by: routes.py/loadLesson, gameTerminal(), reTestWrongWords()
def startGame(lessonFile):
    global wordBank
    global wordBankKeys
    with open(lessonFile + '.json') as jsonFile:
        wordBank = json.load(jsonFile)
    wordBankKeys = list(wordBank.keys())

# function name: getLanguageFolder()
#parameters:
#application: open VocabQuiz/Languages and return folder contents (ie GermanToSpanish, GermantoEnglish, etc)
#outputs/return values: VocabQuiz/Languages/folderName
#called by:
def getLanguageFolder():
    #change the current working directory to the given path
    os.chdir("/Users/alecschwartz/Desktop/workspace/VocabQuiz/Languages")
    folderNames = glob.glob("*")
    return folderNames

# function name: getVocabFiles()
# parameters: language
# application: get existing .json fileNames vocab dictionaries when \
# user selects a language in routes.py/loadLesson
# outputs/return values: fileNames
# called by: routes.py/selectLesson
def getVocabFiles(userSelection):
    #change the current working directory to the given path
    os.chdir("/Users/alecschwartz/Desktop/workspace/VocabQuiz/Languages/" + userSelection)
    fileNames = glob.glob("*.json")
    fileNames = [filename.strip('.json') for filename in fileNames]
    return fileNames

# function name: randomWord()
# parameters: NA
# application: return a random word from wordBank keys
# outputs/return values: random word
# function called by: routes.py/quizPage
def randomWord():
    return random.sample(wordBankKeys, 1)[0]

# function name: answer()
# parameters: vocabTerm
# application: uses key (vocabTerm) to extract value (correctAnswer) in dictionary (wordBank)
# outputs/return values: correctAnswer
# function called by: routes.py/quizPage
def answer(vocabTerm):
    correctAnswer = wordBank[vocabTerm]
    return correctAnswer

# function name: approximateAnswer()
# parameters:
# application: strips away articles from userAnswer/correctAnswer to make user's answer more flexible for this game
# outputs/return values: strippedAnswer
# function called by:


# TODO: find synonymn for approximate
# TODO: split answer by "/" and ....
def cleanString(stringToClean):

    #extraneous stuff to clean away
    articles = ["the","an", "a"]
    punctuation = [".", ",", ":", ";", "?"]

    stringToClean = stringToClean.lower()
    stringToClean.split()
    for x in articles:
        stringToClean = stringToClean.replace(x, "")
    for x in punctuation:
        stringToClean = stringToClean.replace(x, " ")
    stringToClean.join(stringToClean)

    stringToClean = stringToClean.strip()
    return stringToClean




    #### The following lines of code provide for local use of Quiz Game in Terminal ####
# ---------------------------------------------------------------------------------------------------------
# function name: quizSingleWord()
# parameters: vocabTerm, correctAnswer
# application: quizzes user on vocabTerm and compares userAnswer to correctAnswer
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


#function name: numRandomWords()
#parameters: num
#application: apply randomWord() for particular number of words user chooses to be quizzed on
#function called by: gameTerminal()
def numRandomWords(num):
    return random.sample(wordBankKeys, num)

#function name: createTimeStamp()
#parameters: NA
#application: creates a timeStampString for naming files created using createFlashCardSet()
#outputs/return values: returns timeStampString
#function called by: createTimeStamp()

def createTimeStamp():
    timeStamp = datetime.now()
    timeStampString = str(timeStamp.year) + str(timeStamp.month) + str(timeStamp.day) + "_" + str(timeStamp.hour) + "." + str(timeStamp.minute)
    return timeStampString

#function name: createFlashCardSet()
#parameters: NA
#application: allows user to create a new JSON file of a new flashcard set
#outputs/return values: NA
#function called by: "__main__"
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
        print("adding %s : %s\n" % (newTerm, newDefinition))
        newCardSet[newTerm] = newDefinition
    cardSetFile = createTimeStamp() + "_" + setName + ".json"
    with open(cardSetFile, "a+") as file:
        json.dump(newCardSet, file)

# function name: accessFiles()
# parameters: NA
# application: prints flashcard set file names, asks user to select one for quiz,\
    # opens that file and begins gameTerminal()
# outputs/return values: NA
# function is called by: gameTerminal()
def accessFiles():
    #search within directory for JSON files
    os.chdir("/Users/alecschwartz/Desktop/workspace/VocabQuiz")
    # TODO don't need loop
    for file in glob.glob("*.json"):
        print(file)
    answer = input("Which flashcard set would you like to open? \n")
    with open(answer) as jsonFile:
        wordBank = json.load(jsonFile)
    wordBankKeys = list(wordBank.keys())

# function name: gameTerminal()
# parameters: NA
# application: asks user how many words from flashcard set they would like to be quizzed on; \
#   runs startGame() to select vocab file and initialize wordBank;\
#   compares userAnswer to correctAnswer; creates new JSON file and appends wrong wrongs for re-testing later
# outputs/return values: N/A
# function is called by: "__main__"

# TODO: revise this since it's changed for Flask
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

# function name: reTestWrongWords()
# parameters: fileName
# application: run startGame(); open wrongWords text file; user quizSingleWord() to iterate through word bank
# outputs/return values: N/A
# function is called by: wordBank.py
# TODO: revise this since it's changed for Flask

def reTestWrongWords(fileName):
    reQuiz = input("Would you like to be quizzed on the words you missed? Y/N ")
    if reQuiz in ["Y", "y", "YES", "yes"]:
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
