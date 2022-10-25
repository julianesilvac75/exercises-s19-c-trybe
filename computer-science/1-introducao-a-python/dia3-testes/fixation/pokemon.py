import json


def retrieve_pokemons_by_type(type, reader):
    # le o conteudo de reader e o transforma de json para dicionario
    pokemons = json.load(reader)["results"]
    # filtra somente os pokemons do tipo escolhido
    pokemons_by_type = [
        pokemon for pokemon in pokemons if type in pokemon["type"]
    ] 
    return pokemons_by_type