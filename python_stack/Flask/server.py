from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!";

@app.route('/Champion')
def print_champion():
    return "Champion"  

@app.route('/say/<name>')
def hi_name(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<word>')
def repeat(num,word):
    return (word + " ")*num

@app.errorhandler(404)
def page_not_founf(e):
    return "Sorry! No response. Try again."


if __name__ == '__main__':
    app.run(debug=True)