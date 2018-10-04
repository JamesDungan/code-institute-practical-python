from flask import Flask, session, render_template, redirect, request, jsonify, url_for
import libs.gameEngine as engine
import inspect as i
import json
app = Flask(__name__)
app.secret_key = "test"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/initGame', methods=['POST'])
def initGame():

    player1 = request.form["player1"]
    player2 = request.form["player2"]
    player3 = request.form["player3"]
    players = [player1]
    
    if player2 is not '':
        players.append(player2)
    if player3 is not '':
        players.append(player3)

    # if 'categories' not in session:
    engine.startGame(players)
    
        
    return render_template("game.html")

@app.route('/game', methods=['POST'])
def submit_answer():
    print(request.form)
    clueId = request.form.get('clueId')
    value = request.form.get('value')
    pAnswer = request.form.get('pAnswer')
    clueAnswer = request.form.get('clueAnswer')

    result = engine.checkAnswer(clueAnswer, pAnswer)
    engine.updateScore(value, session['currentPlayer'], result)
    engine.disableClue(clueId)
    newRound = False
    session['disabled'] = 30
    if session['disabled'] == 30:
        engine.createNewRound(session['round'] + 1)
        newRound = True

    return render_template("game.html", result=result, newRound=newRound)
    
if __name__ == '__main__':
    app.run(host = 'localhost',
    port = 8080,
    debug = True)

    