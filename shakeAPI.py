#https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application
# https://www.tutorialspoint.com/flask/flask_variable_rules.htm
# James Skon, Kenyon 2022

from textindex import textindex

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

fileName="shakespeare.txt"
sIndex=textindex(fileName)
  
@app.route("/shake/<word>")
def main(word):
    matches=sIndex.lookupLinesJSON(word)
    #print(matches)
    return matches

@app.route("/shake")
def about():
  return "shake/word"
