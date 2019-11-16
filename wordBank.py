#Next steps:
#1) load new json file for wrong words list
#2) comment everything new
#3) camelCase everything (functions and variables and everything)
#4) name variables like "isUserCorrect"

import json
import random
# create instances of wordbank and wordbankkeys
wordbank = {}
wordbankkeys = []

# function name: startgame
# inputs aka parameters: NA
# application: load JSON dictionary as a variable; create global variables for use across multiple functions;
# create list of wordbank keys so they can be shuffled in random_word function
# outputs/return values: NA
# this function is called by: routes.py/quizpage
def startgame():
    global wordbank
    global wordbankkeys
    with open('test.json') as json_file:
        wordbank = json.load(json_file)
    wordbankkeys = list(wordbank.keys())
    # print("this word bank contains {} German words for translation".format(str(len(wordbank))))


# function name: random_word
# inputs aka parameters: NA
# application: shuffle wordbank keys and return random word
# outputs/return values: random german word from wordbank
# this function is called by: routes.py/quizpage
def random_word():
    return wordbankkeys[random.randint(0, len(wordbankkeys)-1)]


#
def quizsingleword(german_word, correct_answer):
    user_answer = input("What does {} mean in English? ".format(german_word))

    if correct_answer == user_answer:
        print("correct! {} means {}".format(german_word, user_answer))
        return True
    elif correct_answer != user_answer:
        print("incorrect. {} means {}".format(german_word, correct_answer))
        return False

# function name: answer
# inputs aka parameters: german_word, user_answer
# application: retrieves the correct_answer from wordbank for comparison to user_answer
# outputs/return values: returns right answer
# this function is called by: routes.py/quizpage
def answer(german_word):
    correct_answer = wordbank[german_word]
    return correct_answer




# function name: game_terminal
# inputs aka parameters: NA
# application: allows for local use; retrieves input for user_answer; compares user_answer to german_word;
              #creates instances of count and correct variables and tracks user performance;
              #creates wrong_words list for re-testing
# outputs/return values: N/A
# this function is called by: wordBank.py
def game_terminal():
    startgame()
    random_word()

    file = open("wrongWordsFromDate.txt", "a+")

    quizwordnum = int(input("How many words would you like to be quizzed on? "))

    for i in range(quizwordnum):
        german_word = random_word()
        correct_answer = answer(german_word)
        userIsCorrect = quizsingleword(german_word, correct_answer)
        if userIsCorrect == False:
            file.write('"{}":"{},"'.format(german_word, correct_answer))


def retest_wrongwords():
    requiz = input("Would you like to be quizzed on the words you missed? Y/N ")
    if requiz in ["Y", "y", "YES", "yes", "yas"]:
        startgame()
        file = open("wrongWordsFromDate.txt", "r")

        #here is where I want to call the original json dict by the wrong words list
        for i in file:
            #set i equal to german_word and use answer function
            german_word = i
            correct_answer = answer(german_word)
            quizsingleword(german_word, correct_answer)

    else:
        print("Good work! See you next time. ")
        quit()

if __name__=="__main__":
    game_terminal()
    retest_wrongwords()
