from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    a = randint(1,100)
    b = randint(1,100)
    return render_template('app02/index.html',
        a=a,
        b=b
    )

app.run(debug=True, port=8000)

