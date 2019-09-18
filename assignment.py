import requests
import json
location = input('Enter the location:')
url = \
    'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=' \
    + location \
    + '&inputtype=textquery&fields=geometry&key=AIzaSyA5mnz61Aj1WoqRagpSy9IlR6pyXGVNiSY'
data = json.loads(requests.get(url).content)
for candidate in data['candidates']:
    lat = candidate['geometry']['location']['lat']
    lng = candidate['geometry']['location']['lng']
    main_url = \
        'https://api.weather.com/v2/turbo/vt1dailyForecast?apiKey=d522aa97197fd864d36b418f39ebb323&format=json&geocode=' \
        + str(lat) + '%2C' + str(lng) + '&language=en-IN&units=m'
    info = requests.get(main_url)
    weather_info = json.loads(info.text)
    day_info = weather_info['vt1dailyForecast']['day']['dayPartName']
    temp_info = weather_info['vt1dailyForecast']['day']['temperature']
    thunderstroms_info = weather_info['vt1dailyForecast']['day']['narrative']
    forcasts = list()
    for weather_news in zip(day_info, temp_info, thunderstroms_info):
        forcasts.append({'Day': weather_news[0],
                        'Temprature': weather_news[1], 'Thunderstorms_News': weather_news[2]})

for item in forcasts:
    print(item)
