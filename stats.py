import requests


def get_stats(country):
    url = 'https://covid-193.p.rapidapi.com/statistics'

    querystring = {'country': country}

    headers = {
        'x-rapidapi-host': 'covid-193.p.rapidapi.com',
        'x-rapidapi-key': 'READ README TO GET THE RAPIDAPI KEY'
    }

    r = requests.get(url, headers=headers, params=querystring)

    try:
        data = r.json()

        country = data['parameters']['country']
        date = '.'.join(data['response'][0]['day'].split('-'))
        new = 'no data given' if not data['response'][0]['cases']['new'] else data['response'][0]['cases']['new']
        active = data['response'][0]['cases']['active']
        critical = 'no data given' if not data['response'][0]['cases'][
            'critical'] else data['response'][0]['cases']['critical']
        deaths = data['response'][0]['deaths']['total']
        recovered = data['response'][0]['cases']['recovered']
        total = data['response'][0]['cases']['total']

        text = f'{country} on {date}:\n\n◉ New cases: {new}\n◉ Active cases: {active}\n◉ Critical cases: {critical}\n◉ Recovered: {recovered}\n◉ Total deaths: {deaths}\n◉ Total cases: {total} '
        return text

    except:
        print(r.text)
        return f'No data for {country}'
