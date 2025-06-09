# WeatherApp
Weather App – Tech Assessment 1
This is a simple weather app built with Python (Flask) that lets users enter a location (city or ZIP code) and get real-time weather data using the OpenWeatherMap API.

It also includes a 5-day forecast, and supports using the user's current location (to be added later).

✅ Features
🔍 Enter a location (City name or ZIP code) to get weather
🌤 Shows current weather (temperature, humidity, wind, etc.)
📅 Includes a 5-day weather forecast
🌐 Uses real weather data via the OpenWeatherMap API
🖼 Weather icons from OpenWeatherMap for better visuals

📋 Requirements
Python 3.x
Flask
Requests
OpenWeatherMap API Key

🚀 How to Run This App
1. Clone this repository
git clone https://github.com/yourusername/weather-app-flask.git
cd weather-app-flask

2. Set up the virtual environment
python -m venv venv
Activate it:
Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate

3. Install the dependencies
pip install -r requirements.txt
If there's no requirements.txt, you can install manually:
pip install flask requests

4. Set your API Key
In app.py, replace this line:
API_KEY = "your_api_key_here"
With your real API key from https://openweathermap.org/api.

5. Run the app
python app.py
Open your browser and go to:
http://127.0.0.1:5000

📦 File Structure
weather-app-flask/
│
├── app.py                 # Main Flask app
├── templates/
│   └── index.html         # UI layout with form and weather display
├── venv/                  # Virtual environment (not committed)
└── README.md              # This file
