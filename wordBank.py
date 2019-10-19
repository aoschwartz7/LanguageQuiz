import json
import random

wordbank = {}
wordbankkeys = []

#load JSON dictionary as a variable:
def startgame():
    global wordbank
    global wordbankkeys
    with open('test.json') as json_file:
        wordbank = json.load(json_file)
    wordbankkeys = list(wordbank.keys())
    random.shuffle(wordbankkeys)

def random_word():
    return wordbankkeys[0]

if __name__=="__main__":
    startgame()
