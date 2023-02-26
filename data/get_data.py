# Program for automatically getting results from the most recent F1 race and then
# using the result to calculate points depending on the user's predictions.

# Importing the necessary modules
import requests
import json
import sqlite3


# for i in range(0, 23):
#     response = requests.get(f"http://ergast.com/api/f1/2022/{i}/results.json")
#     data = response.json()

#     # Get race name from data
#     race_name = data["MRData"]["RaceTable"]["Races"][0]["raceName"]



#     # races and results X refers to the order and starts with 0
#     winner = data["MRData"]["RaceTable"]["Races"][0]["Results"][0]["Driver"]["familyName"]
#     second = data["MRData"]["RaceTable"]["Races"][0]["Results"][1]["Driver"]["familyName"]
#     third = data["MRData"]["RaceTable"]["Races"][0]["Results"][2]["Driver"]["familyName"]
#     fourth = data["MRData"]["RaceTable"]["Races"][0]["Results"][3]["Driver"]["familyName"]
#     fifth = data["MRData"]["RaceTable"]["Races"][0]["Results"][4]["Driver"]["familyName"]
#     sixth = data["MRData"]["RaceTable"]["Races"][0]["Results"][5]["Driver"]["familyName"]

# Insert data into the tables
# Insert data into the rasmus table
#c.execute("INSERT INTO rasmus VALUES (1, 'Bahrain Grand Prix', ?, ?, ?, ?, ?, ?)", (lewis, mav, valtteri, lando, carlos, charles))
