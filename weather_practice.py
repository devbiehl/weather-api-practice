import json
import urllib.request

# create a list of cities
cities = [
    {'name': 'Indianapolis', 'lat': 39.7684, 'lon': -86.1581},
    {'name': 'Hilton Head Island', 'lat': 32.2163, 'lon': -80.7526},
    {'name': 'Gulf Shores', 'lat': 30.2460, 'lon': -87.7008},
    {'name': 'Las Cruces', 'lat': 32.3199, 'lon': -106.7637},
    {'name': 'Austin', 'lat': 30.2672, 'lon': -97.7431},
    {'name': 'New York', 'lat': 40.7128, 'lon': -74.0060}
]

weather_list = []

# loop through cities to fetch weather
for city in cities:
    lat = city['lat']
    lon = city['lon']
    name = city['name']

    #url builder
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true'

    response = urllib.request.urlopen(url)
    data = response.read().decode()

    weather = json.loads(data)

    #print(json.dumps(weather, indent=4))

    # get weather info 
    current = weather.get('current_weather', {})
    temp_c = current.get('temperature', None)
    windspeed = current.get('windspeed', 'N/A')

    # convert to Fehrenheit
    if temp_c is not None:
        temp_f = (temp_c * 9/5) + 32
    else:
        temp_f = None
    
    # append list
    weather_list.append({
        'name': name,
        'temp_c': temp_c,
        'temp_f': temp_f,
        'windspeed': windspeed
    })
# sort by Temp F descending
sorted_weather = sorted(weather_list, key=lambda t: t['temp_f'] if t['temp_f'] is not None else -9999, reverse=True)

for w in sorted_weather:
    print(f"{w['name']}: {w['temp_f']:.1f} F ({w['temp_c']}) C, Wind: {w['windspeed']} km/h")