import requests
from twilio.rest import Client

# Make a request to the OpenWeatherMap API to get the weather in Germantown for the next 12 hours if it will rain and the current weather
# Send a text message to my phone if it will rain in the next 12 hours and tell me to carry an umbrella
# Send a text message to my phone with the current weather in Germantown

API_KEY = ""
account_sid = ""
auth_token = ""

conn = requests.get("https://api.openweathermap.org/data/2.5/forecast?q=Germantown,us&units=metirc&appid=" + API_KEY)
data = conn.json()
weather_data = data["list"]
weather_slice = weather_data[:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
         body="It's going to rain today. Remember to bring an umbrella!",
         from_='+18555460690',
         to='+12407965270'
         )
    print(message.status)
