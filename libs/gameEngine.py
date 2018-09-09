import random
import requests
from datetime import datetime as dt
base_url = "http://www.jservice.io/api/"

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class Game:
    def __init__(self, names, categories):
        self.player1= Player(names[0])

        if len(names) > 1:
            self.player2= Player(names[1])
        if len(names) > 2:
            self.player3= Player(names[2])

        self.categories = categories

def initRound(rNumber):
    categoriesFull = getRandomCategories()
    rCategories = []
    while len(rCategories) <= 6:
        category = fetchCategory(categoriesFull, rNumber)
        # make sure no repetition
        if category not in rCategories:
            rCategories.append(category)
    return rCategories

def initGame(names):
    rCategories = initRound(1)
    game = Game(names, rCategories)
    return game


def getRandomCategories():
    offset = random.randint(1, 183)*100
    print(offset)
    response = requests.get(base_url+"categories?count=100&offset="+str(offset))
    return response.json()

# assert getRandomCategories()  == [], "empty list"

# check category id against previous chosen
# choose a random category from the initial 100
# call api/category endpoint to get the category data
# store this in category variable
# store category.clues[] in list and shuffle

# create empty clue list
# create two lists of strings ('ROUND1/ROUND2') - one for each round - ['two','four','six','eight','one-thousand'],['four','eight','twelve','sixteen','two-thousand']
# assign live variable to one of these depending on which round is being played
# loop through the clues list while round1/round2 list size is >= 0 
        # at each itteration
            #loop through round1/round2 list
                # if value is not null and still present in round1/round2 list - else break (next clue)
                    # check question not null
                    # check answer not null
                    # if all checks pass - else break (next clue)
                        # place in (empty) clue list - position depending on amount
                        # remove corresponding index from round1/round2

# create variable for each amount (200,400,600,800,1000 if round 1 // 400,800,1200,1600,2000 if round 2)
# choose the first amount and check validity
# check if clue exists for each amount 
# check if all clues have questions and answer

# receives a list of categories and picks one at random
# sends this to the clueValidator which sends back its valid clues (of which there must be 5)
def fetchCategory(categories, round):
    rClues = []
    while len(rClues) < 5:
        randomIndex = random.randint(0, 99)
        categoryId = categories[randomIndex]['id']
        response = requests.get(base_url+"category?id="+str(categoryId))
        category = response.json()
        categoryTitle = category['title']

        clues = category['clues'] #-->list of dicts
        random.shuffle(clues)
        
        jpyrdy1 = [200,400,600,800,1000]
        jpyrdy2 = [400,800,1200,1600,2000]
        
        if round == 1:
            rValues = jpyrdy1
        elif round == 2:
            rValues = jpyrdy2

        rClues = clueValidator(clues, rValues, rClues)
    rCategory = {'title':categoryTitle, 'clues':rClues}    
    return rCategory
    

# receives list of clues and round-values and empty list of clues for the round
# returns list of all the valid clues matching the values from the round-values list (one for each value)
def clueValidator(clues, rValues, rClues):
    for clue in clues:
        for index, val in enumerate(rValues):
            newGameDate = dt.strptime("2001-11-01T12:00:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ")
            airdate = dt.strptime(clue['airdate'], "%Y-%m-%dT%H:%M:%S.%fZ")
            if airdate > newGameDate:
                if clue['value'] == val:
                    if clue['answer'] is not None and clue['question'] is not None:
                        rClues.append(clue)
                        rValues.remove(val)
                        break
    return rClues






