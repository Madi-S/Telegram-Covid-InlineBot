import requests

url = "https://covid-193.p.rapidapi.com/countries"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "e3a8dbeca1mshfffc2e32f1bef5dp161597jsn03514351c7bb"
}

r = requests.get(url, headers=headers).json()['response']


class Searcher:
    def __init__(self):
        self.countries = requests.get(
            url, headers=headers).json()['response']

    def search(self, country):
        if country in self.countries:
            return True

        return False

