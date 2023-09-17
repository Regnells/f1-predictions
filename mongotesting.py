import pymongo
import creds

# Start connection to mongoDB
client = pymongo.MongoClient("192.168.10.36", 27017, username="f1Admin", password=creds.password, authSource="f1")

# create database instance
db = client.f1

# create collection instance
collection = db.martin

# Find winners of race in collection, exclude _id
#result = collection.find_one({"_id": "Bahrain"}, {"_id": 0})
#for key in result:
#    print(result[key])

# Set up guesses
hamilton = "Hamilton"
verstappen = "Verstappen"
perez = "Perez"
norris = "Norris"
leclerc = "Leclerc"
sainz = "Sainz"
russsel = "Russel"
stroll = "Stroll"
vettel = "Vettel"
ocon = "Ocon"
gasly = "Gasly"
piastri = "Piastri"
alonso = "Alonso"



race = "BelgiumSprint"
bahrain = "Bahrain"
saudi = "Saudi"
australia = "Australia"
azerbaijan = "Azerbaijan"
azerbaijansp = "AzerbaijanSprint"
miami = "Miami"
monaco = "Monaco"
spain = "Spain"
canada = "Canada"
austria = "Austria"
austriasp = "AustriaSprint"
england = "England"
hungary = "Hungary"
belgium = "Belgium"
belgiumsp = "BelgiumSprint"
netherlands = "Netherlands"
italy = "Italy"

# create document list
races = [
    {"_id": netherlands, "winner": verstappen, "second": hamilton, "third": perez, "fourth": alonso, "fifth": russsel, "sixth": leclerc},
    {"_id": italy, "winner": verstappen, "second": perez, "third": sainz, "fourth": alonso, "fifth": hamilton, "sixth": russsel}
]

# insert document
#collection.insert_many(races)

collection.update_one({"_id": italy}, {"$set": {"winner": verstappen, "second": sainz, "third": perez, "fourth": leclerc, "fifth": hamilton, "sixth": alonso}})

#find all documents in collection
result = collection.find()
for document in result:
    print(document)

# close connection
client.close()