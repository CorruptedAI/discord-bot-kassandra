import requests


class OpenWeather:
    def __init__(self, city, token):
        address = "http://api.openweathermap.org/data/2.5/weather?appid="
        self.feelsrainman = requests.get(f"{address}{token}&q={city}").json()
        if self.feelsrainman["cod"] == "404":
            print("---\ncity not found\n---\n")
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
        return self.feelsrainman["weather"]["0"]["main"]

    def get_description(self):
        return self.feelsrainman["weather"]["0"]["description"]

    def get_icon(self):
        return self.feelsrainman["weather"]["0"]["icon"]

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
        pass

    def get_humidity(self):
        pass

    def get_visibility(self):
        pass

    # k - km/h
    # m - m/s
    def get_wind_speed(self, s="k"):
        pass

    def get_wind_deg(self):
        pass

    def get_clouds(self):
        pass

    def get_dt(self):
        pass

    def get_country(self):
        pass

    def get_sunrise(self):
        pass

    def get_sunset(self):
        pass

    def get_timezone(self):
        pass

    def get_name(self):
        pass
