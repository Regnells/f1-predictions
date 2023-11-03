from app import app
from app.mongo.MongoData import MongoData
from app.forms import guessForm
from flask import render_template, url_for


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/standings', methods=['GET'])
def standings():
    mongo = MongoData()
    standings = mongo.user_points().sort("totalPoints", -1)
    #mongo.close()
    return render_template('standings.html', title='Standings', standings=standings)

@app.route('/tip', methods=['GET', 'POST'])
def tip():
    mongo = MongoData()
    form = guessForm()

    if form.validate_on_submit():
        mongo.add_user_guess(form.race.data, form.user.data, form.first.data, form.second.data, form.third.data, form.fourth.data, form.fifth.data, form.sixth.data)

    return render_template('tip.html', title='Tip', form=form)