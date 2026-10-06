from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"

@app.route("/minside")
def minside():
    print("dette skriver jeg ut med print")
    return "nå er jeg på minside"


@app.route("/endaenside")
def endaenside():
    return "dette er enda en side"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)    