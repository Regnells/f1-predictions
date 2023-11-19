from app import app
from app.mongo.MongoData import MongoData
from app.forms import guessForm
from flask import render_template, url_for, request


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

@app.route('/compare', methods=['GET', "POST"])
def compare():
    mongo = MongoData()
    
    users = mongo.get_users()
    races = mongo.get_races()
    input_user = request.form.get('selectUser')
    input_race = request.form.get('selectRace')
    # Variables declared here to avoid error when page is loaded
    user_guess = None
    race_result = None
    standings = mongo.user_points().sort("totalPoints", -1)

    if request.method == 'POST':
        user_guess = mongo.get_user_guess(input_race, input_user)
        race_result = mongo.get_race_result(input_race)


    return render_template('compare.html', title="Jämför", 
                           users=users, 
                           races=races, 
                           input_user=input_user, 
                           input_race=input_race, 
                           user_guess=user_guess, 
                           race_result=race_result,
                           standings=standings)
