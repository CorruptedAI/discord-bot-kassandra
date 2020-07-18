import requests


class ExchangeRates:
    def __init__(self, base, currency, amount=1):
        address = "https://api.exchangeratesapi.io/latest"
        self.exchange = requests.get(f"{address}?base={base.upper()}").json()
        self.currency = currency.upper()
        self.amount = amount

    def get_rate(self):
        return self.exchange["rates"][self.currency] * self.amount

    def get_date(self):
        return self.exchange["date"]
