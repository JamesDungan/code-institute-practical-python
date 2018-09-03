import random
import requests
base_url = "http://www.jservice.io/api/"


def getRandomCategories():
    offset = random.randint(1, 183)*100
    print(offset)
    response = requests.get(base_url+"categories?count=100&"+offset)
    print(response.json())
# assert getRandomCategories()  == [], "empty list"

getRandomCategories()