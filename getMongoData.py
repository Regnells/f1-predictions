import pymongo
import config

class MongoData:
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
    
    def getGuess(self, race, winner, second, third, fourth, fifth, sixth):
        race_guess = [race, winner, second, third, fourth, fifth, sixth]
        return race_guess
    
    def addGuess(self, user, guess):
        user = user.lower()

        match user:
            case "anton":
                self.anton.insert_one({"_id": guess[0], "winner": guess[1], "second": guess[2], "third": guess[3], "fourth": guess[4], "fifth": guess[5], "sixth": guess[6]})
            case "rasmus":
                self.rasmus.insert_one({"_id": guess[0], "winner": guess[1], "second": guess[2], "third": guess[3], "fourth": guess[4], "fifth": guess[5], "sixth": guess[6]})
            case "martin":
                self.martin.insert_one({"_id": guess[0], "winner": guess[1], "second": guess[2], "third": guess[3], "fourth": guess[4], "fifth": guess[5], "sixth": guess[6]})
            case "jesper":
                self.jesper.insert_one({"_id": guess[0], "winner": guess[1], "second": guess[2], "third": guess[3], "fourth": guess[4], "fifth": guess[5], "sixth": guess[6]})
            case "result":
                self.winner.insert_one({"_id": guess[0], "winner": guess[1], "second": guess[2], "third": guess[3], "fourth": guess[4], "fifth": guess[5], "sixth": guess[6]})
            case _:
                print("Something went wrong")

    def getPoints(self, user):
        races = ["Bahrain", "Saudi", "Australia", "AzerbaijanSprint", "Azerbaijan", "Miami", "Monaco", "Spain", "Canada", "AustriaSprint", "Austria", "England", "Hungary", "BelgiumSprint", "Belgium", "Netherlands", "Italy", "Singapore", "Japan"]
        points = 0

        user = user.lower()
    
        for race in races:
            guess = ""
            match user:
                case "anton":
                    guess = self.antonguess(race)
                case "rasmus":
                    guess = self.rasmusguess(race)
                case "martin":
                    guess = self.martinguess(race)
                case "jesper":
                    guess = self.jesperguess(race)

            result = mongo.topsix(race)

            length = len(guess)

            for i in range(0, length):
                if guess[i] == result[i]:
                    points += 2
                elif guess[i] in result:
                    points += 1
                else:
                    None
        return f'{user} has {points} points'

        

    


# test
if __name__ == "__main__":
    # mongo = MongoData()
    # guess = mongo.getGuess("Japan", "Verstappen", "Norris", "Piastri", "Leclerc", "Hamilton", "Sainz")
    # mongo.addGuess("result", guess)
    # mongo.close()
    mongo = MongoData()
    print(mongo.getPoints("jesper"))
    print(mongo.getPoints("anton"))
    print(mongo.getPoints("martin"))
    print(mongo.getPoints("rasmus"))
    mongo.close()

            
