from flask import Flask, session, render_template, redirect, request, jsonify, url_for
import libs.gameEngine as engine
import inspect as i
import json
app = Flask(__name__)
app.secret_key = "test"
@app.route('/')
def index():
    session.clear()
    session['round'] = 1
    return render_template("index.html")

@app.route('/initRound', methods=['GET','POST'])
def initRound():
    if session['round'] == 1:
        player1 = request.form["player1"]
        player2 = request.form["player2"]
        player3 = request.form["player3"]
        players = [player1]
        
        if player2 is not '':
            players.append(player2)
        if player3 is not '':
            players.append(player3)

        engine.startGame(players)
    return render_template("game.html")

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
    if len(session['disabled']) == 30:
        session.pop('disabled')
        leader = engine.getLeader()
        leaderName = leader['leaderName']
        leaderPoints = leader['leaderPoints']
        if session['round'] == 1:
            session['round']+=1
            session.modified = True
            engine.createNewRound(session['round'])
            thisRound = 'two'
        elif session['round'] == 2:
            thisRound = 'end'
        return render_template("summary.html", result=result, thisRound=thisRound, leaderName = leaderName, leaderPoints = leaderPoints)

    return render_template("game.html", result=result)





if __name__ == '__main__':
    app.run(host = 'localhost',
    port = 8080,
    debug = True)

    