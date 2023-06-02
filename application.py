from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def main():
    with open("PageFiles/index.html") as f:
        return f.read()