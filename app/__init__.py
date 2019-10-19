from flask import Flask
# from wordBank import startgame

app = Flask(__name__) #creates instance of Flask

from app import routes #now imports routes module; kept as bottom line of code so app object can be established first

# startgame()
