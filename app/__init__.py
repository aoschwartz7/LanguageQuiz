from flask import Flask
# first create Flask instance:
app = Flask(__name__)
# now use routes.py
from app import routes
