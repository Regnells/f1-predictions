from app import app
from app.mongo.MongoData import MongoData
from flask import render_template, url_for


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/standings')
def standings():
    mongo = MongoData()
    standings = mongo.users_total_points().sort("totalPoints", -1)
    #mongo.close()
    return render_template('standings.html', title='Standings', standings=standings)

@app.route('/tip')
def tip():
    return render_template('tip.html', title='Tip')