from app import app
from app.mongo.getMongoData import MongoData
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    mongo = MongoData()
    jesper = (mongo.getPoints("jesper"))
    anton = (mongo.getPoints("anton"))
    martin = (mongo.getPoints("martin"))
    rasmus = (mongo.getPoints("rasmus"))
    mongo.close()

    return render_template('index.html', title='Home', jesper=jesper, anton=anton, martin=martin, rasmus=rasmus)

