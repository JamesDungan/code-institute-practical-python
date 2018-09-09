from flask import Flask, render_template
import libs.gameEngine as engine

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/game')
def game():
    game = engine.initGame(['john', 'paul', 'george'])
    return render_template("game.html", game=game)

# @app.route('/leader_board')
# def leader_board():
#     return render_template("index.html")


if __name__ == '__main__':
    app.run(host = 'localhost',
    port = 8080,
    debug = True)

    