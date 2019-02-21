# Practical Python Project

Welcome to J'Pyrdy!
J'Pyrdy! is an online emulation of the U.S. television quiz show Jeopardy! It was developed using the python programming language and makes use of the jService api which feeds the application with over 150,000 trivia questions from the popular game show. J'Pyrdy can be played in single or multi player mode with payers choosing clues and answering qeustions in succession.
 
## UX

The aim of this site is to provide users with a palyable web-based version of the TV game show Jeopardy!, accessible and playable via any browser. In order to provide a genuine experience, it was decided from the project's inception that every effort would be made to reproduce the gameplay, as well as the look and feel of the game board as accurately as possible. Using the jService api as the source of the game questions goes a long way in helping achieve this. Likewise, the choice of fonts and colours is vital in ensuring the game is a true and accurate representation of the look and feel of the original TV show.

### User Stories

- As a player, I want to play a game so that I can win!
- As a player, I want to look at the leader-board so that I can see the top scoring players.
 
### Design process documents 

- [MockFlow](https://wireframepro.mockflow.com/view/M2e3fef52f030d73d9107cc14eabb60381534878022416)

## Features
 
### Existing Features

- Welcome page
- New round generator. Creates new round by calling api to retrieve data and populates game board template.
- Game board. Displays clue-values and categories. Clickable interface to facilitate gameplay.
- Leader board file generator. Creates or amends leader board file with top 10 scores.
- Leader-board. Displays top 10 players and their scores.


#### Gameplay
- When they first arrive, users will be presented with a welcome message and form in which they can choose the number of players for the next game and enter their names. Clicking the button will commence play.
- Players will be presented with the ROUND 1 (J'Pyrdy!) game board where hidden clues and values will be populated in a grid. Six categories will line the top of the board, each with five amounts in the column below. Player One will proceed to play by clicking on an amount in any category.
- When an amount is clicked a corresponding clue is revealed along with a text area in which they an enter their answer, a submit button and a count-down timer (counting down from 10 seconds). A correct answer will add the value of the chosen clue to the players score. An incorrect answer will deduct this value from the players score. The value will also be deducted if the player runs out of time.
- The game continues as above with each player taking a turn until all clue-values have been chosen.
- Players will then be presented with the ROUND 2 (Double J'Pyrdy!) game board. Play repeats in the same manner as round 1 until all clue-values have been chosen.

### Features Left to Implement
- Double Jeopardy
- Ability for players in multiplayer game to buzz when they know the answer instead of just waiting their turn
- Final Joepardy round

## Technologies Used

- [python3](https://www.python.org/downloads/)
    - The python programming language was used to develop the game engine and server on the backend

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation. 

- [flask](http://flask.pocoo.org/docs/1.0/#user-s-guide)
    - The **Flask** web development micro-framework was used on the back end. 


## Deployment

### Heroku

The site was deployed to Heroku via new branch (production) which was based on the master branch. The app.secret_key was stored as a heroku config var. 
Finally a Procfile was created for gunicorn which points to the app itself `web: gunicorn run:app`


### Locally

If you would like to run this code locally, follow these instructions:

1. Clone the repository 
  * (with ssh) `git@github.com:JamesDungan/code-institute-practical-python.git` 
  * (with https) `https://github.com/JamesDungan/code-institute-practical-python.git`
2. Open the folder in your favorite IDE
3. Install [python3](https://www.python.org/downloads/) on your machine 
4. Open a terminal and from the root of this project create a virtual environment where you will install all of your dependencies
5. Then activate the virtual environment and run `pip install -r requirements.txt` from the root of the project.
6. You will have to create a local .env file to store the following variable: `APP_SECRET_KEY`   
6. Now that all of your dependancies have been installed you can run the app by running `python3 run.py`