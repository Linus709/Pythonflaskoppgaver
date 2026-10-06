from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def forside():
    return render_template("base.html")

@app.route("/bluepage")
def blue():
    return render_template("bluethepage.html")

@app.route("/greenpage")
def green():
    return render_template("greenthepage.html")

@app.route("/redpage")
def red():
    return render_template("redthepage.html")

@app.route("/data")
def data():
    num = random.random()
    print(num)
    return render_template("meddata.html", sendesInn = num)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

#oppgave1done
#oppgave2done
#oppgave3done