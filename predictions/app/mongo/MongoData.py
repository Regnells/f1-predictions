import pymongo
import config

class MongoData:
    def __init__(self):
        # create client instance
        self.client = pymongo.MongoClient("192.168.10.36", 27017, username=config.username, password=config.password, authSource=config.authSource)
        # create database instance
        db = self.client.f1

        # set up class variables
        self.races = db.userGuess
        self.users = db.users

    def close(self):
        self.client.close()

    # Get winners from race, returns list of winners.
    def top_six(self, race):
        race = race.lower()
        query = self.races.find_one({"_id": race.lower()}, {"_id": 0})
        result_list = [value for key, value in query['result'].items()]
        return result_list
        
    def user_guess(self, race, user):
        race = race.lower()
        user = user.lower()
        query = self.races.find_one({"_id": race}, {"_id": 0})
        result_list = [value for key, value in query[user].items()]
        return result_list
    
    def calculate_points(self, user):
        races = ["bahrain", "saudi", "australia", "azerbaijansprint", "azerbaijan", "miami", "monaco", "spain", "canada", "austriasprint", "austria", "england", "hungary", "belgiumsprint", "belgium", "netherlands", "italy", "singapore", "japan"]
        user = user.lower()
        points = 0
        for race in races:
            actual_result = self.top_six(race)
            user_prediction = self.user_guess(race, user)
            for i in range(0, len(user_prediction)):
                if user_prediction[i] == actual_result[i]:
                    points += 2
                elif user_prediction[i] in actual_result:
                    points += 1
                else:
                    None
        self.users.update_one({"_id": user}, {"$set": {"points": points}})



# test
if __name__ == "__main__":
    # Get winner of race "race" from collection "userGuess"
    mongo = MongoData()
    mongo.calculate_points("jesper")