import requests


class Weather:

    def __init__(self):

        city = input("Enter city name: ")

        self.get_coordinates(city)

    def get_coordinates(self, city):

        url = "https://geocoding-api.open-meteo.com/v1/search"

        params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        response = requests.get(url, params=params)

        data = response.json()

        print(data)


weather = Weather()