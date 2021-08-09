from flask import Flask
import requests


app = Flask(__name__)


@app.route("/")
def hello():
    return "success"

@app.route("/car-list")
def car_list():
    url = 'https://fms-dev-api.carbom.co.kr/fms/v1/caro/car'
    response = requests.get(url,
                            headers = {"accept": "application/json; charset=utf-8", "Content-Type": "application/json; charset=utf-8",
                                         "Authorization": "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjYXJvQGNhcm8uY28ua3IiLCJhdWQiOiJhdXRoVG9rZW47Rk1TVXNlcjsiLCJpYXQiOjE2MjYyNDc0MTEsImV4cCI6MTYyODgzOTQxMSwiY29tcGFueV9pZCI6MTA0LCJicmFuY2hfaWQiOjQwMn0.KEeSQ4BIMNIXXapF7zCkXGVwYDydlejuS3bkZoZQIsw"},
                            )

    return response.status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0')
