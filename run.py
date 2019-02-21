from flask import Flask, session, render_template, redirect, request, jsonify, url_for
import libs.gameEngine as engine
import inspect as i
import json
import os

app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET_KEY')

@app.route('/')
def index():
    session.clear()
    session['round'] = 1
    return render_template("index.html")

@app.route('/initRound', methods=['GET','POST'])
def initRound():
    if session['round'] == 1:
        header = "Round 1 J'Pyrdy!"
        player1 = request.form["player1"]
        player2 = request.form["player2"]
        player3 = request.form["player3"]
        players = [player1]
        
        if player2 is not '':
            players.append(player2)
        if player3 is not '':
            players.append(player3)

        engine.startGame(players)
    else:
        header = "Round 2 Double J'Pyrdy!"   
    return render_template("game.html", header = header)

@app.route('/game', methods=['POST'])
def submit_answer():
    clueId = request.form.get('clueId')
    value = request.form.get('value')
    pAnswer = request.form.get('pAnswer')
    clueAnswer = request.form.get('clueAnswer')

    result = engine.checkAnswer(clueAnswer, pAnswer)
    engine.updateScore(value, session['currentPlayer'], result)
    engine.disableClue(clueId)
    thisRound=""
    if session['round'] == 1:
        header = "Round 1 J'Pyrdy!"
    else:
        header = "Round 2 Double J'Pyrdy!"
    if len(session['disabled']) == 30:
        session.pop('disabled')
        leader = engine.getLeader()
        score = leader['score']
        name = leader['name']
        if session['round'] == 1:
            session['round']+=1
            session.modified = True
            engine.createNewRound(session['round'])
            thisRound = 'two'
        elif session['round'] == 2:
            thisRound = 'end'
            engine.updateLeaderBoard()
        return render_template("summary.html", result=result, thisRound=thisRound, name = name, score= score, header = "Game Summary" )

    return render_template("game.html", result=result, header=header)

@app.route('/leader_board', methods=['GET'])
def leader_board():
    header="Leader Board"
    leaderBoard = engine.getLeaderBoard()
    return render_template("leaderBoard.html", leaderBoard=leaderBoard, header=header)



if __name__ == '__main__':
    app.run(host = 'localhost',
    port = 8080,
    debug = True)

# if __name__ == '__main__':
#     app.run(host = os.getenv('IP', '0.0.0.0'),
#     port = os.getenv('PORT', 8080),
#     debug = True)
    