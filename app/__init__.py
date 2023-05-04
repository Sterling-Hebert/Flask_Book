from flask import Flask, session

from .config import Config

app = Flask(__name__)

app.config.from_object(Config)


@app.route("/")
def index():
    visits()
    return "Tweeter"


@app.route('/visits-counter/')
def visits():
    if 'visits' in session:
        # reading and updating session data
        session['visits'] = session.get('visits') + 1
    else:
        # setting session data
        session['visits'] = 1
    return "Total visits: {}".format(session.get('visits'))


@app.route('/delete-visits/', methods=["POST"])
def delete_visits():
    session.pop('visits', None)  # delete visits
    return 'Visits deleted'
