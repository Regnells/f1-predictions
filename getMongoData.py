import pymongo
import config

class GetMongoData:
    def __init__(self):
        # create client instance
        self.client = pymongo.MongoClient("192.168.10.36", 27017, username=config.username, password=config.password, authSource="f1")
        # create database instance
        db = self.client.f1

        # set up class variables
        self.winner = db.winners
        self.anton = db.anton
        self.martin = db.martin
        self.rasmus = db.rasmus
        self.jesper = db.jesper

    def close(self):
        self.client.close()

    def topsix(self, race):
        winners = []
        race = race
        result = self.winner.find_one({"_id": race}, {"_id": 0})
        for key in result:
            winners.append(result[key])
        return winners
        
    def antonguess(self, race):
        race = race
        guess_list = []
        gueses = self.anton.find_one({"_id": race}, {"_id": 0})
        for key in gueses:
            guess_list.append(gueses[key])
        return guess_list

    def rasmusguess(self, race):
        race = race
        guess_list = []
        gueses = self.rasmus.find_one({"_id": race}, {"_id": 0})
        for key in gueses:
            guess_list.append(gueses[key])
        return guess_list

    def martinguess(self, race):
        race = race
        guess_list = []
        gueses = self.martin.find_one({"_id": race}, {"_id": 0})
        for key in gueses:
            guess_list.append(gueses[key])
        return guess_list
    
    def jesperguess(self, race):
        race = race
        guess_list = []
        gueses = self.jesper.find_one({"_id": race}, {"_id": 0})
        for key in gueses:
            guess_list.append(gueses[key])
        return guess_list

# test
if __name__ == "__main__":
    mongo = GetMongoData()
    races = ["Bahrain", "Saudi", "Australia", "AzerbaijanSprint", "Azerbaijan", "Miami", "Monaco", "Spain", "Canada", "AustriaSprint", "Austria", "England", "Hungary", "BelgiumSprint", "Belgium", "Netherlands", "Italy"]
    points = 0
    
    for race in races:
        guess = mongo.antonguess(race)
        result = mongo.topsix(race)

        length = len(guess)

        for i in range(0, length):
            if guess[i] == result[i]:
                points += 2
            elif guess[i] in result:
                points += 1
            else:
                None
        print(f'After race: {race}, player has this many points: {points}')
    print(f'User has {points} points')
    mongo.close()

            
