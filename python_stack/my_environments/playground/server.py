from flask import Flask , render_template
app = Flask(__name__)

#level 1
@app.route('/play')
def play():
    return render_template("index.html", times=3, color="#9fc5f8")

#level 2
@app.route('/play/<int:x>')
def play_x(x):
    return render_template("index.html", times=x, color="#9fc5f8")

#level3
@app.route('/play/<int:x>/<color>')
def play_color(x,color):
    return render_template("index.html", times=x, color=color)


if __name__ == '__main__':
    app.run(debug=True)