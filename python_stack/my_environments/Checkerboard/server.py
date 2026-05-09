from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", row=8, col=8)

@app.route("/<int:x>")
def row_only(x):
    return render_template("index.html", row=x, col=8)

@app.route("/<int:x>/<int:y>")
def custom_board(x, y):
    return render_template("index.html", row=x, col=y)

if __name__ == "__main__":
    app.run(debug=True)