from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "0e474ab42e475d9834233b5bd30d3153"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather(location):
    params = {"q": location, "appid": API_KEY, "units": "metric"}
    response = requests.get(WEATHER_URL, params=params)
    return response.json()

def get_forecast(location):
    params = {"q": location, "appid": API_KEY, "units": "metric"}
    response = requests.get(FORECAST_URL, params=params)
    return response.json()

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    forecast_data = None

    if request.method == "POST":
        location = request.form.get("location")
        if location:
            weather_data = get_weather(location)
            forecast_data = get_forecast(location)

    return render_template("index.html", weather=weather_data, forecast=forecast_data)

if __name__ == "__main__":
    app.run(debug=True)

