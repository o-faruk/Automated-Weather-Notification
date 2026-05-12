# Automated Weather Notification

A Python app that fetches real-time weather data and sends a daily push notification to your phone with temperature, humidity, and wind speed. Could be automated for other things but currently set for daily weather data.

## Demo

> "Good Morning!
> Current Weather in Norwich CT:
> Temperature: 58.42 °F
> Relative Humidity: 72%
> Wind Speed: 14.3 m/s"

Delivered straight to your phone via Pushover.

---

## Features

- Fetches live weather data from the [Open-Meteo API](https://open-meteo.com/)
- Sends push notifications to iOS, Android, or desktop via [Pushover](https://pushover.net/)
- Scheduled to run at any interval (every morning, every hour, etc.)
- Temperature conversion from Celsius to Fahrenheit built in
- Lightweight — no database, no frontend, just Python

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Open-Meteo API | Free weather data (no key required) |
| Pushover API | Push notifications to mobile/desktop |
| `schedule` | Task scheduling |
| `requests` | HTTP requests |

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/o-faruk/Automated-Weather-Notification.git
cd Automated-Weather-Notification
```

### 2. Install dependencies

```bash
pip install requests schedule
```

### 3. Set up Pushover

- Create a free account at [pushover.net](https://pushover.net/)
- Create an application to get your **API token**
- Grab your **user key** from your dashboard

### 4. Set your credentials as environment variables

**Do not hardcode your API keys in the source code.**

```bash
# Mac/Linux
export PUSHOVER_TOKEN="your_token_here"
export PUSHOVER_USER="your_user_key_here"

# Windows
set PUSHOVER_TOKEN=your_token_here
set PUSHOVER_USER=your_user_key_here
```

### 5. Set your location

In `weather.py`, update the latitude and longitude to your location:

```python
latitude = 41.5304   # your latitude
longitude = -72.0631 # your longitude
```

You can find your coordinates at [latlong.net](https://www.latlong.net/).

### 6. Run it

```bash
python weather.py
```

---

## How It Works

1. The scheduler triggers `send_weather_update()` at your set interval
2. The app calls the Open-Meteo API with your coordinates
3. It parses temperature, humidity, and wind speed from the response
4. It formats a friendly message and sends it via the Pushover API to your device

---

## Configuration

| Variable | Description |
|---|---|
| `latitude` / `longitude` | Your location coordinates |
| `schedule.every(15).seconds` | Change to `.minutes`, `.hours`, or `.days` as needed |

---

## Future Improvements

- [ ] Support multiple locations
- [ ] Add weather condition descriptions (sunny, cloudy, rainy)
- [ ] Daily forecast summary (not just current hour)
- [ ] Email notification support as an alternative to Pushover
- [ ] Environment variable loading via `.env` file with `python-dotenv`

---

## Security Note

Never commit API keys or user tokens to GitHub. Always use environment variables or a `.env` file. Add `.env` to your `.gitignore`:

```
.env
PUSHOVER_TOKEN=your_token_here
PUSHOVER_USER=your_user_key_here
```

---

## Author

**Omar Faruk** — CS Undergraduate @ University of Connecticut
[GitHub](https://github.com/o-faruk)
