import schedule
import time
import requests
import http.client
import urllib

#Receives Data From Open Meteo API and returns data
def get_weather(latitude, longitude):
    try:
        base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Uses PushOver API to send notifications to IPhone/Android/Desktop
def send_push_notification(body):
    try:
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
                     urllib.parse.urlencode({
                         "token": "##############################",
                         "user": "##############################",
                         "message": body,
                     }), { "Content-type": "application/x-www-form-urlencoded" })
        
        response = conn.getresponse()
        print("Push notification sent! Status:", response.status)
    except Exception as e:
        print(f"Error sending push notification: {e}")

# Assigns Data from Open Meteo to variables and prints the PushOver MSG 
def send_weather_update():
    # Hardcoded latitude and longitude for Norwich, CT
    latitude = 41.530426593020444
    longitude = -72.06317805795109
    
    # Receives Weather data from API
    weather_data = get_weather(latitude, longitude)
    if weather_data:
        temperature_celsius = weather_data['hourly']["temperature_2m"][0]
        relative_humidity = weather_data['hourly']["relativehumidity_2m"][0]
        wind_speed = weather_data['hourly']['windspeed_10m'][0]
        temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
        
        #Prints Message 
        weather_info = (
            f"Good Morning!\n"
            f"Current Weather in Norwich CT:\n"
            f"Temperature: {temperature_fahrenheit:.2f} °F\n"
            f"Relative Humidity: {relative_humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
        
        send_push_notification(weather_info)

#Sends a PushOver Notification Every x Seconds/Minutes/Days
def main():
    schedule.every(15).seconds.do(send_weather_update)  # Set to every 2 seconds for testing
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    #send_weather_update()  # Direct call for immediate test
    main()
    
    #Notes
    # Possibly able to use for other things
    # Can send to other devices
    # Currently set to 2 seconds until stopped

