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

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
