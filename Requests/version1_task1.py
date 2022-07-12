import requests

heroes = ['Hulk', 'Captain America', 'Thanos']


def find_id(name: str, token='2619421814940190'):
    url = f"https://superheroapi.com/api/{token}/search/{name}"
    response = requests.get(url, timeout=5)
    return response.json()['results'][0]['id']


def hero_request(name: str, param_compare='intelligence', token='2619421814940190'):
    id_character = find_id(name)
    url = f'https://superheroapi.com/api/{token}/{id_character}/powerstats'
    response = requests.get(url, timeout=5)
    param_compare_value = response.json()[param_compare]
    return {name: int(param_compare_value)}


def compare_heroes(name_hero_list: list):
    heroes_power = {}
    for name in name_hero_list:
        heroes_power.update(hero_request(name))
    return max(heroes_power, key=heroes_power.get)


print('Кто самый умный супергерой?:')
print(compare_heroes(heroes))
