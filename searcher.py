import requests

url = 'https://covid-193.p.rapidapi.com/countries'

headers = {
    'x-rapidapi-host': 'covid-193.p.rapidapi.com',
    'x-rapidapi-key': 'READ README TO GET THE RAPIDAPI KEY'
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

