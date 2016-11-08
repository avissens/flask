from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/jedi/<firstname>/<secondname>")
def hi_person(firstname, secondname):
    name = secondname[:3] + firstname[:2]
    name = name.title()
    return render_template('template.html', my_name=name)
                           
if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))