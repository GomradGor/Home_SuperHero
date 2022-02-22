import requests


TOKEN = '2619421814940190'
superhero_list = ['Hulk', 'Thanos', 'Captain America']

def intellect_find(hero_list):
    super = []
    for hero in hero_list:
        url = f'https://www.superheroapi.com/api.php/{TOKEN}/search/{hero}'  # Формируем строку запроса
        intellect = requests.get(url).json()  # Данные Героев в формате .JSON
        # print(intellect)
        try:
            for power in intellect['results']:
                super.append({
                    'name': power['name'],
                    'intelligence': power['powerstats']['intelligence'],
                })
        except :
            print(f"Ошибка. Проверьте список супергероев: {hero_list}")

    intelligence_super_hero = 0  # Отсчет интелекта
    name = ''
    for intelligence_hero in super:
        if intelligence_super_hero < int(intelligence_hero['intelligence']):
            intelligence_super_hero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f"Самый умный супергерой: {name}, его интелект: {intelligence_super_hero}")


if __name__ == '__main__':

    intellect_find(superhero_list)