from flask import Flask, render_template, request
import libs.gameEngine as engine
import inspect as i
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/game', methods=['POST'])
def game():
    player1 = request.form.get("player1")
    player2 = request.form.get("player2")
    player3 = request.form.get("player3")
    players = [player1,player2,player3]
    
    game = engine.initGame(players)
    
    return render_template("game.html", game=game)

# @app.route('/leader_board')
# def leader_board():
#     return render_template("index.html")


if __name__ == '__main__':
    app.run(host = 'localhost',
    port = 8080,
    debug = True)

    