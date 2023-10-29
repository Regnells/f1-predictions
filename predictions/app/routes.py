from app import app
from app.mongo.MongoData import MongoData
from flask import render_template, url_for


@app.route('/')
@app.route('/index')
def index():
    standings = "test"
    return render_template('index.html', title='Home', standings=standings)

