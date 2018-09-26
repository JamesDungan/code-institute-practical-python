from flask import Flask, session, render_template, request
import libs.gameEngine as engine
import inspect as i
app = Flask(__name__)
app.secret_key = "test"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/game', methods=['POST'])
def game():

    player1 = request.form["player1"]
    player2 = request.form["player2"]
    player3 = request.form["player3"]
    players = [player1]
    
    if player2 is not '':
        players.append(player2)
    if player3 is not '':
        players.append(player3)

    engine.initGame(players)
    
    #todo: think about keeping track of game board data in session 
    #       and reload game board every time player submits an answer
    #todo: 
        
    return render_template("game.html")

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    category = request.form.get('category')
    value = request.form.get('value')
    pAnswer = request.form.get('pAnswer')
    clueAnswer = request.form.get('clueAnswer')

    result = engine.checkAnswer(clueAnswer, pAnswer)
    #call update score 
    #return result (corect/incorrect) with new scores to game template (received by success function)
    return ('', 204)
    





if __name__ == '__main__':
    app.run(host = 'localhost',
    port = 8080,
    debug = True)

    