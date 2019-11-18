#Next steps:
#1) rename wordBank.py

import json
import random
from datetime import datetime

# create instances of wordBank and wordBankKeys
wordBank = {}
wordBankKeys = []
wrongWords = {}

# function name: startgame
# parameters: NA
# application: load JSON dictionary as a variable; create global variables for use across multiple functions;
# create list of wordbank keys so they can be shuffled in random_word function
# outputs/return values: NA
# this function is called by: routes.py/quizpage, gameTerminal(), reTestWrongWords()
def startGame():
    global wordBank
    global wordBankKeys
    with open('test.json') as jsonFile:
        wordBank = json.load(jsonFile)
    wordBankKeys = list(wordBank.keys())

# function name: random_word
# parameters: NA
# application: shuffle wordbank keys and return random word
# outputs/return values: random german word from wordbank
# function called by: routes.py/quizpage
def randomWord():
    return random.sample(wordBankKeys, 1)[0]

#function name: numRandomWords
#parameters: num
#application: apply randomWord() for particular number of words user chooses to be quizzed on
#function called by: gameTerminal()
def numRandomWords(num):
    return random.sample(wordBankKeys, num)

# function name: quizSingleWord
# parameters: germanWord, correctAnswer
# application: quizzes user on germanWord; compares userAnswer to correctAnswer
# outputs/return values: Boolean T/F
# function called by: gameTerminal(), reTestWrongWords()
def quizSingleWord(germanWord, correctAnswer):
    userAnswer = input("What does {} mean in English? ".format(germanWord))
    if userAnswer == correctAnswer:
        print("correct! {} means {}".format(germanWord, userAnswer))
        return True
    elif userAnswer != correctAnswer:
        print("incorrect. {} means {}".format(germanWord, correctAnswer))
        return False

# function name: answer
# parameters: german_word, user_answer
# application: retrieves the correct_answer from wordbank for comparison to user_answer
# outputs/return values: returns right answer
# function is called by: routes.py/quizpage, gameTerminal(), reTestWrongWords()
def answer(germanWord):
    correctAnswer = wordBank[germanWord]
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
# def createFlashCardSet(newTerm, newDefinition):
#     newTerm = input("Enter new term: ")
#     newDefinition = input("Enter definition for term: ")


# function name: gameTerminal
# parameters: NA
# application: for local use; retrieves input for userAnswer; compares userAnswer to germanWord; creates text file and appends wrong wrongs for re-testing
# outputs/return values: N/A
# function is called by: wordBank.py
def gameTerminal():
    startGame()
    quizWordNum = int(input("How many words would you like to be quizzed on? "))
    miniWordBank = numRandomWords(quizWordNum)
    for i in range(quizWordNum):
        germanWord = miniWordBank[i]
        correctAnswer = answer(germanWord)
        userIsCorrect = quizSingleWord(germanWord, correctAnswer)
        if userIsCorrect == False:
            wrongWords[germanWord] = correctAnswer
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
            germanWord = i
            correctAnswer = answer(germanWord)
            quizSingleWord(germanWord, correctAnswer)
    else:
        print("Good work! See you next time. ")
        quit()

if __name__=="__main__":
    gameTerminal()
