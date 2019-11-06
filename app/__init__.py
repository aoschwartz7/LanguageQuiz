from flask import Flask
#first create Flask instance:
app = Flask(__name__)
from app import routes
