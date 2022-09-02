from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

DB_HOST = ''
DB_USER = ''
DB_PASSWORD = ''
DB_NAME = ''

client = MongoClient(DB_HOST, username=DB_USER, password=DB_PASSWORD)
db = client[DB_NAME]

def get_temperatures():
    temperatures = db.temperatures
    return list(temperatures.find())[-20:]

def cal_diff(temps):
    old_temp = temps[0]['t']
    for item in temps:
        item['diff'] = item['t'] - old_temp
        old_temp = item['t']

@app.route("/")
def index():
    temperatures = get_temperatures()
    if len(temperatures) > 0:
        cal_diff(temperatures)

    return render_template("app05/index.html",
        temperatures=temperatures
    )

@app.route("/tempform", methods=['GET','POST'])
def temp_form():
    if request.method == 'POST':
        t = float(request.form['t'])

        temperatures = db.temperatures
        temperatures.insert_one({ 't': t })

        return redirect("/")

    return render_template("app05/tempform.html")

app.run(debug=True, port=8000)