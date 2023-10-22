import requests
# https://api.openweathermap.org/data/2.5/weather?q=S%C3%A3o%20Pedro,BR&appid=45edc20f3b1af893dccc4cc23244bf3b&units=metric
def get_web_weather_info(city, country):
    api_key = '45edc20f3b1af893dccc4cc23244bf3b'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            air_humidity = data['main']['humidity']
            air_temperature = data['main']['temp']
            return [air_humidity, air_temperature]
        else:
            return f'Erro na solicitação: {data["message"]}'
    except Exception as e:
        return f'Erro ao obter dados: {str(e)}'