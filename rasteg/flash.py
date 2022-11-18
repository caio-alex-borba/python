from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    quest = 'a'
    return quest

if __name__ == "__main__":
    app.run()