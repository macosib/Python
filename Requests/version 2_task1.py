import requests

heroes = ['Hulk', 'Captain America', 'Thanos']


def hero_request(name: str, param_compare='intelligence', token='2619421814940190'):
    url = f"https://superheroapi.com/api/{token}/search/{name}"
    response = requests.get(url, timeout=5)
    value_param_compare = response.json()['results'][0]['powerstats'][param_compare]
    return {name: int(value_param_compare)}


def compare_heroes(heroes: list):
    heroes_power = {}
    for hero in heroes:
        heroes_power.update(hero_request(hero))
    return max(heroes_power, key=heroes_power.get)


print('Кто самый умный супергерой?:')
print(compare_heroes(heroes))
