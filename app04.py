from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

def random_problem():
    return randint(1,100), randint(1,100)

@app.route("/", methods=['GET','POST'])
def index():
    message = ''
    if request.method == 'POST':
        a = int(request.form.get('a','0'))
        b = int(request.form.get('b','0'))
        answer = int(request.form.get('answer','0'))
        if a + b == answer:
            message = "Correct!"
            a,b = random_problem()
        else:
            message = "Incorrect, please try again."
    else:
        a,b = random_problem()

    return render_template('app04/index.html',
        message=message,
        a=a,
        b=b
    )

app.run(debug=True, port=8000)

