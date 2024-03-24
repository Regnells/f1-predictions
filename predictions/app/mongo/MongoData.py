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
    
    def get_races(self):
        races = [
            "bahrain", "saudi arabia", "australia",
            "japan", "china", "chinaSprint",
            "miami", "miamiSprint", "imola",
            "monaco", "canada", "spain", "austria",
            "austriaSprint", "Silverstone", "hungary",
            "spa", "spaSprint", "netherlands",
            "monza", "azerbaijan", "singapore",
            "texas", "texasSprint", "mexico",
            "brazil", "brazilSprint", "las vegas",
            "qatar", "qatarSprint", "abu dhabi"
        ]
        return races
    
    # Remove all raced races
    def get_future_races(self):
        raced_races = self.get_raced_races()
        future_races = self.get_races()
        for i in raced_races:
            future_races.remove(i)
        return future_races
    
    def get_raced_races(self):
        races = []
        for i in self.userGuess.find({"result": {"$exists": "true"}}, {"_id": 1}):
            races.append(i["_id"])
        return races
        
    # Get winners from race, returns list of winners.
    def get_race_top_six(self, race):
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
    
    def get_user_top_drivers(self, user):
        user = user.lower()
        query = self.users.find_one({"_id": user}, {"top10Drivers": 1})
        drivers_list = [value for key, value in query['top10Drivers'].items()]
        return drivers_list
    
    def get_user_top_constructors(self, user):
        user = user.lower()
        query = self.users.find_one({"_id": user}, {"top10Constructors": 1})
        constructors_list = [value for key, value in query['top10Constructors'].items()]
        return constructors_list

    # Returns all users and their points
    def get_all_user_points(self):
        points = self.users.find({}, {"top10Drivers": 0, "top10Constructors": 0})
        return points
    
    def get_user_points(self, user):
        user = user.lower()
        points = self.users.find_one({"_id": user}, {"_id": 0, "points": 1, "penalty": 1})
        return points
    
    # Stuff broke at some point
    # def calculate_points(self, user):
    #     races = self.get_races()
    #     user = user.lower()
    #     points = 0
    #     for race in races:
    #         actual_result = self.top_six(race)
    #         user_prediction = self.get_user_guess(race, user)
    #         for i in range(0, len(user_prediction)):
    #             if user_prediction[i] == actual_result[i]:
    #                 points += 2
    #             elif user_prediction[i] in actual_result:
    #                 points += 1
    #             else:
    #                 None
    #     self.users.update_one({"_id": user}, {"$set": {"points": points}})

    # def set_total_points(self, user):
    #     points = self.users.find_one({"_id": user.lower()}, {"points": 1})
    #     penalty = self.users.find_one({"_id": user.lower()}, {"penalty": 1})
    #     total_points = points['points'] - penalty['penalty']
    #     self.users.update_one({"_id": user.lower()}, {"$set": {"totalPoints": total_points}})

    # Quick explanation of rules:
    # If user guesses the correct driver in the correct position, 2 points are awarded.
    # If user guesses the correct driver in top 6, 1 point is awarded.
    def calculate_user_points(self):
        races = self.get_raced_races()
        users = self.get_users()
        for user in users:
            points = 0
            for race in races:
                result = self.get_race_top_six(race)
                guess = self.get_user_guess(race, user)
                for i in range(0, len(guess)):
                    if guess[i] == result[i]:
                        points += 2
                    elif guess[i] in result:
                        points += 1
                    else:
                        None
            self.users.update_one({"_id": user}, {"$set": {"points": points}})

    def update_user_total(self):
        users = self.get_users()
        for user in users:
            points = self.get_user_points(user)
            total = points["points"] - points["penalty"]
            self.users.update_one({"_id": user}, {"$set": {"totalPoints": total}})
    
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
        
    def add_penalty(self, user):
        user = user.lower()
        self.users.update_one({"_id": user}, {"$inc": {"penalty": +5}})

# test
if __name__ == "__main__":
    mongo = MongoData()
    print(mongo.get_raced_races())
    mongo.close()