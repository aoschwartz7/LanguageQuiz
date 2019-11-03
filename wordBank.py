import json
import random

wordbank = {}
wordbankkeys = []

# user_answer = input("type answer here")

#load JSON dictionary as a variable:
def startgame():
    global wordbank
    global wordbankkeys
    with open('test.json') as json_file:
        wordbank = json.load(json_file)
    wordbankkeys = list(wordbank.keys())

def random_word():
    return wordbankkeys[random.randint(0, len(wordbankkeys))]

# function name: answer
# inputs aka parameter: german_word, user_answer
# what it does unless this is obvious: gets correct_answer from wordbank, compares user_answer to correct_answer
# outputs aka return values: returns True or False
# this function is called by:
def answer(german_word, user_answer):
    correct_answer = wordbank[german_word]
    if user_answer == correct_answer:
        return correct_answer
    else:
        return correct_answer

if __name__=="__main__":
    startgame()
