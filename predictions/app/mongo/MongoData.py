import pymongo
from app.mongo import mongoconfig
#import mongoconfig

class MongoData:
    def __init__(self):
        # create client instance
        self.client = pymongo.MongoClient(mongoconfig.host, mongoconfig.port, username=mongoconfig.username, password=mongoconfig.password, authSource=mongoconfig.authSource)
        # create database instance
        db = self.client.f1

        # set up class variables
        self.users = db[mongoconfig.users]
        self.userGuess = db[mongoconfig.guess]

    def close(self):
        self.client.close()

    def get_users(self):
        find_users = self.users.find({}, {"_id": 1})
        users = []
        for user in find_users:
            users.append(user["_id"])
        return users

    def get_races(self):
        get_races = self.userGuess.find({}, {"_id": 1})
        races = []
        for race in get_races:
            races.append(race['_id'])
        return races
    
    # Get winners from race, returns list of winners.
    def top_six(self, race):
        race = race.lower()
        query = self.userGuess.find_one({"_id": race.lower()}, {"_id": 0})
        result_list = [value for key, value in query['result'].items()]
        return result_list
        
    def get_user_guess(self, race, user):
        race = race.lower()
        user = user.lower()
        query = self.userGuess.find_one({"_id": race}, {"_id": 0})
        # Getting the actual race from the query
        result_list = [value for key, value in query[user].items()]
        return result_list
    
    def get_race_result(self, race):
        user = "result"
        race = race.lower()
        query = self.userGuess.find_one({"_id": race}, {"_id": 0})
        # Getting the actual race from the query
        result_list = [value for key, value in query[user].items()]
        return result_list
    
    def calculate_points(self, user):
        races = self.get_races()
        user = user.lower()
        points = 0
        for race in races:
            actual_result = self.top_six(race)
            user_prediction = self.get_user_guess(race, user)
            for i in range(0, len(user_prediction)):
                if user_prediction[i] == actual_result[i]:
                    points += 2
                elif user_prediction[i] in actual_result:
                    points += 1
                else:
                    None
        self.users.update_one({"_id": user}, {"$set": {"points": points}})

    def add_penalty(self, user):
        user = user.lower()
        self.users.update_one({"_id": user}, {"$inc": {"penalty": +5}})

    def set_total_points(self, user):
        points = self.users.find_one({"_id": user.lower()}, {"points": 1})
        penalty = self.users.find_one({"_id": user.lower()}, {"penalty": 1})
        total_points = points['points'] - penalty['penalty']
        self.users.update_one({"_id": user.lower()}, {"$set": {"totalPoints": total_points}})

    def user_points(self):
        points = self.users.find({})
        return points
    
    def add_result(self, race, first, second, third, fourth, fifth, sitxth):
        race = race.lower()
        self.userGuess.insert_one({"_id": race.lower(), 
                                   "result": {"first": first.lower(), 
                                              "second": second.lower(), 
                                              "third": third.lower(), 
                                              "fourth": fourth.lower(), 
                                              "fifth": fifth.lower(), 
                                              "sixth": sitxth.lower()}})
    
    def add_user_guess(self, race, user, first, second, third, fourth, fifth, sitxth ):
        self.userGuess.update_one(
                {"_id": race},
                {"$set": {user: {"first": first, 
                                 "second": second, 
                                 "third": third, 
                                 "fourth": fourth, 
                                 "fifth": fifth, 
                                 "sixth": sitxth} } },
                upsert=True
            )

    # I'm just lazy and will keep all drivers here, no use for them in the
    # database yet
    def get_drivers(self):
        drivers = [
            "verstappen","perez", "russell", "hamilton",
            "leclerc", "sainz", "pastri", "norris",
            "stroll", "alonso", "ocon", "gasly",
            "albon", "sargeant", "ricciardo", "tsunoda",
            "bottas,", "zhou", "magnussen", "hulkenberg"
        ]
        return drivers
# test
if __name__ == "__main__":
    # Get winner of race "race" from collection "userGuess"
    mongo = MongoData()
    mongo.close()