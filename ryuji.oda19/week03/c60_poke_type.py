import requests


# import json

def poke_type(attribute):
    # rep = open('pokemon.json')
    # data = json.load(rep)
    rep = requests.get('https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json')
    data = rep.json()
    LIST = []
    # type = ['Fire','Water']
    getdict = data['pokemon']
    # print(getdict)

    for i in getdict:

        if len(attribute) == 2:
            if attribute[0] in i['type'] and attribute[1] in i['type']:
                LIST.append((i['id'], i['name']))

        elif len(attribute) == 1:
            if attribute[0] in i['type']:
                LIST.append((i['id'], i['name']))
    return LIST

# print(poke_type(['Psychic','Water']))
# print(poke_type([]))
