from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", row=8, col=8)

@app.route("/<int:x>")
def row_only(x):
    return render_template("index.html", row=x, col=8)

@app.route("/<int:x>/<int:y>/<color1>/<color2>")
def custom_board(x, y, color1, color2):
    return render_template("index.html", row=x, col=y, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)