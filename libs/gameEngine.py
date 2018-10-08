import random
import requests
import operator
from flask import session 
from datetime import datetime as dt
import base64
base_url = "http://www.jservice.io/api/"

def startGame(names):

    rCategories = initRound(session['round'])
    session['categories'] = rCategories
    
    players = [{'number':1, 'name':names[0], 'score':0}]

    if len(names) > 1:
        players.append({'number':2, 'name':names[1], 'score':0})
    if len(names) > 2:
        players.append({'number':3, 'name':names[2], 'score':0})
    session['players'] = players    
    session['currentPlayer'] = 1

def initRound(rNumber):
    categoriesFull = getRandomCategories()
    rCategories = []
    while len(rCategories) <= 5:
        category = fetchCategory(categoriesFull, rNumber)
        # make sure no repetition
        if not any(category['title'] == c['title'] for c in rCategories):
            rCategories.append(category)
    return rCategories

def createNewRound(rNumber):
    rCategories = initRound(rNumber)
    session['categories'] = rCategories
    session['currentPlayer'] = 1

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
        rClues = []
        index = random.randint(0,99)
        categoryId = categories[index]['id']
        response = requests.get(base_url+"category?id="+str(categoryId))
        category = response.json()
        categoryTitle = category['title']

        clues = category['clues'] #-->list of dicts
        random.shuffle(clues)
        
        rValues = [200,400,600,800,1000]

        rClues = clueValidator(clues, rValues, rClues)
        print(len(rClues))
    rClues.sort(key=operator.itemgetter('value'), reverse=True)
    
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
                        #base64 encode answers so they dont show in dev tools
                        string = clue['answer']
                        encodedStr = base64.b64encode(string.encode())
                        clue['answer'] = encodedStr
                        if session['round'] == 2:
                            clue['value']*=2
                        rClues.append(clue)
                        rValues.remove(val)
                        break
    return rClues



def checkAnswer(clueAnswer, pAnswer):
    #automatically return false(incorrect answer) if user enters empty string or space
    if pAnswer == '' or pAnswer == ' ':
        return False
    #remove single quotes and first char 'b' which were added during encoding process
    clueAnswer = clueAnswer.replace("'","")
    clueAnswer = clueAnswer[1:]
    #decode correct answer
    decodedClueAnswer = base64.b64decode(clueAnswer)
    decodedClueAnswer = decodedClueAnswer.decode('ascii')
    #see if user gave correct answer i n their response
    result = decodedClueAnswer.find(pAnswer)
    if result == -1:
        return False
    else:
        return True

def updateScore(value, currentPlayer, result):
    for p in session['players']:
        if p['number'] == currentPlayer:
            if result == True:
                p['score'] += int(value)
                session.modified = True
            else:
                p['score'] -= int(value)
                session.modified = True
    if session['currentPlayer'] < len(session['players']):
        session['currentPlayer'] += 1
    else:
        session['currentPlayer'] = 1

def disableClue(clueId):
    if 'disabled' not in session:
        session['disabled']=[int(clueId)]
        session.modified = True
    else: 
        session['disabled'].append(int(clueId))
        session.modified = True

def getLeader():
    if len(session['players'] == 1):
        leader = {'leaderName':session['players'][0]['name'], 'leaderPoints':session['players'][0]['score']}
        return leader

    # max_score = max(player['score'] for player in players)
    for p in session['players']:


        
                
#session['players'] = {players:[{'number':1, 'name':names[0], 'score':0},{'number':1, 'name':names[0], 'score':0}]}




