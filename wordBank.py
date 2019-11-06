#Next steps: modify this file so user can play game locally from terminal
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

# function name: random_word
# inputs aka parameters: NA
# application: shuffle wordbank keys and return random word
# outputs/return values: random german word from wordbank
# this function is called by: routes.py/quizpage
def random_word():
    return wordbankkeys[random.randint(0, len(wordbankkeys))]

# function name: answer
# inputs aka parameters: german_word, user_answer
# application: retrieves the correct_answer from wordbank for comparison to user_answer
# outputs/return values: returns right answer
# this function is called by: routes.py/quizpage
def answer(german_word, user_answer):
    correct_answer = wordbank[german_word]
    return correct_answer

if __name__=="__main__":
    startgame()
