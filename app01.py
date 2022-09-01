from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "<p>Hello, world</p>"

app.run(debug=True, port=8000)

