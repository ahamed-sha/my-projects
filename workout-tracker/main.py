import requests
from datetime import datetime
import os

APP_ID = "535355392894829482"
API_KEY = "24424235636636366"

nutritionix_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("what exercise have you done today?")

nutritionix_config = {
    "query": query
}

nutritionix_response = requests.post(url=nutritionix_endpoint, json=nutritionix_config, headers=nutritionix_header)
data = nutritionix_response.json()
type_of_exercise = data["exercises"][0]["user_input"]
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]

today = datetime.now()
current_day = datetime.strftime(today, "%d/%m/%Y")
current_time = datetime.strftime(today, "%H:%M:%S")

sheety_endpoint = "https://api.sheety.co/2423874837/workoutTracking/workouts"

sheety_config = {
    "workout": {
        "date": current_day,
        "time": current_time,
        "exercise": type_of_exercise.title(),
        "duration": duration,
        "calories": calories
    }
}

sheety_header = {
    "Authorization": "Bearer 235557744dgdgdgdgdg"
}

sheety_response = requests.post(url=sheety_endpoint, json=sheety_config, headers=sheety_header)
