import requests


class OpenWeather:
    def __init__(self, token, city):
        address = "http://api.openweathermap.org/data/2.5/weather?appid="
        self.feelsrainman = requests.get(f"{address}{token}&q={city}").json()

    def get_error(self):
        if self.feelsrainman["cod"] == "404":
            return True
        elif self.feelsrainman["cod"] == "401":
            print(
                "---\nInvalid API key. Please see http://openweathermap.org/faq#error401 for more info.\n---\n"
            )

    def get_json(self):
        return self.feelsrainman

    def get_coord_lon(self):
        return self.feelsrainman["coord"]["lon"]

    def get_coord_lat(self):
        return self.feelsrainman["coord"]["lat"]

    def get_main(self):
        return self.feelsrainman["weather"][0]["main"]

    def get_description(self):
        return self.feelsrainman["weather"][0]["description"]

    def get_icon(self):
        return self.feelsrainman["weather"][0]["icon"]

    def get_base(self):
        return self.feelsrainman["weather"]["base"]

    # k - Kelvin
    # f - Fahrenheit
    # c - Celsius
    def get_temp(self, s="k"):
        if s == "k":
            return self.feelsrainman["main"]["temp"]
        elif s == "f":
            return (self.feelsrainman["main"]["temp"] - 273.15) * 9 / 5 + 32
        elif s == "c":
            return self.feelsrainman["main"]["temp"] - 273.15
        else:
            print("Invalid argument. Only 'k', 'f' and 'c', 'k' as default")

    def get_feels(self, s="k"):
        if s == "k":
            return self.feelsrainman["main"]["feels_like"]
        elif s == "f":
            return (self.feelsrainman["main"]["feels_like"] - 273.15) * 9 / 5 + 32
        elif s == "c":
            return self.feelsrainman["main"]["feels_like"] - 273.15
        else:
            print("Invalid argument. Only 'k', 'f' and 'c', 'k' as default")

    def get_temp_min(self, s="k"):
        if s == "k":
            return self.feelsrainman["main"]["temp_min"]
        elif s == "f":
            return (self.feelsrainman["main"]["temp_min"] - 273.15) * 9 / 5 + 32
        elif s == "c":
            return self.feelsrainman["main"]["temp_min"] - 273.15
        else:
            print("Invalid argument. Only 'k', 'f' and 'c', 'k' as default")

    def get_temp_max(self, s="k"):
        if s == "k":
            return self.feelsrainman["main"]["temp_max"]
        elif s == "f":
            return (self.feelsrainman["main"]["temp_max"] - 273.15) * 9 / 5 + 32
        elif s == "c":
            return self.feelsrainman["main"]["temp_max"] - 273.15
        else:
            print("Invalid argument. Only 'k', 'f' and 'c', 'k' as default")

    def get_pressure(self):
        return self.feelsrainman["main"]["pressure"]

    def get_humidity(self):
        return self.feelsrainman["main"]["humidity"]

    def get_visibility(self):
        return self.feelsrainman["visibility"]

    # m - m/s
    # k - km/h
    def get_wind_speed(self, s="m"):
        if s == "m":
            return self.feelsrainman["wind"]["speed"]
        elif s == "k":
            return self.feelsrainman["wind"]["speed"] * 3.6
        else:
            print("Invalid argument. Only 'm' and 'k', 'm' as default")

    # d - degree
    # r - radian
    def get_wind_deg(self, s="d"):
        if s == "d":
            return self.feelsrainman["wind"]["deg"]
        elif s == "r":
            PI = 3.141592653589793
            return self.feelsrainman["wind"]["deg"] * PI / 180
        else:
            print("Invalid argument. Only 'd' and 'r', 'd' as default")

    def get_clouds(self):
        return self.feelsrainman["clouds"]["all"]

    def get_data(self):
        return self.feelsrainman["dt"]

    def get_country(self):
        return self.feelsrainman["sys"]["county"]

    def get_sunrise(self):
        return self.feelsrainman["sys"]["sunrise"]

    def get_sunset(self):
        return self.feelsrainman["sys"]["sunset"]

    def get_timezone(self):
        return self.feelsrainman["timezone"]

    def get_name(self):
        return self.feelsrainman["name"]
