import requests

api_key = '67fb74e75cf795bad268237095353284'
city = 'London'

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

response = requests.get(url)
data = response.json()

# Create a structured representation of the data
organized_data = {
    'location': data['name'],
    'weather': {
        'description': data['weather'][0]['description'],
        'temperature': data['main']['temp'],
        'feels_like': data['main']['feels_like'],
        'humidity': data['main']['humidity'],
        'pressure': data['main']['pressure'],
    },
    'wind': {
        'speed': data['wind']['speed'],
        # 'deg' might not always be present
        'degree': data['wind'].get('deg', None),
    },
    'clouds': {
        'cloudiness': data['clouds']['all'],
    },
    'sun': {
        'sunrise': data['sys']['sunrise'],
        'sunset': data['sys']['sunset'],
    },
    # 'visibility' might not always be present
    'visibility': data.get('visibility', None),
    'timestamp': data['dt'],
}

print(organized_data)


html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Report</title>
</head>
<body>
    <h1>Weather Report for {data['name']}</h1>
    <p>Weather: {data['weather'][0]['description']}</p>
    <p>Temperature: {data['main']['temp']}°C</p>
    <p>Feels Like: {data['main']['feels_like']}°C</p>
    <p>Humidity: {data['main']['humidity']}%</p>
    <p>Pressure: {data['main']['pressure']} hPa</p>
    <p>Wind Speed: {data['wind']['speed']} m/s</p>
    <p>Cloudiness: {data['clouds']['all']}%</p>
    <p>Sunrise: {data['sys']['sunrise']}</p>
    <p>Sunset: {data['sys']['sunset']}</p>
    <p>Timestamp: {data['dt']}</p>
</body>
</html>
"""

# Write the HTML content to a file
with open('weather_report.html', 'w') as f:
    f.write(html_content)

print("Weather report HTML file generated successfully.")
