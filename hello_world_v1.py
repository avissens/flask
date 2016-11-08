from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/jedi/<firstname>/<secondname>")
def hi_person(firstname, secondname):
    name = secondname[:3] + firstname[:2]
    return "Hello {}!".format(name.title())

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))