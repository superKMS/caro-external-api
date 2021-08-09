from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "success"

@app.route("/car-list")
def hello():
    return "car-list"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
