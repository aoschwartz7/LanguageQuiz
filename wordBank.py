#Next steps:
#1) modify this file so user can play game locally from terminal
#2) allow user to pick a number of words to be quizzed on
#3) allow user to save their progress as flash card sets (ie terms they've been quizzed on)
#4) incorporate entire dictionary

import json
import random
# create instances of wordbank and wordbankkeys
wordbank = {}
wordbankkeys = []
wrongwords = {}
count = 0
correct = 0

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
    # print(wordbankkeys[random.randint(0, len(wordbankkeys))])
    return wordbankkeys[random.randint(0, len(wordbankkeys))]
# function name: answer
# inputs aka parameters: german_word, user_answer
# application: retrieves the correct_answer from wordbank for comparison to user_answer
# outputs/return values: returns right answer
# this function is called by: routes.py/quizpage
def answer(german_word, user_answer):
    correct_answer = wordbank[german_word]
    return correct_answer

def game_terminal():
    count = 0
    correct = 0
    for word in wordbank:
        user_answer = input("What does {} mean in English?".format(german_word))
        if german_word == user_answer:
            count += 1
            correct += 1
            print("correct! {} means {}".format(german_word, user_answer))
        elif german_word != user_answer:
            count += 1
            wrongwords.append(german_word)
            print("incorrect. {} means {}".format(german_word, wordbank[german_word]))

# def wrongwords():


if __name__=="__main__":
    game_terminal()
