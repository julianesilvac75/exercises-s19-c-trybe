import json
from unittest.mock import mock_open, patch
from pokemon import retrieve_pokemons_by_type
# import pytest
# from io import StringIO


def test_retrieve_pokemons_by_type():
    # definimos um pokemon do tipo grama:
    grass_type_pokemon = {
        "national_number": "001",
        "evolution": None,
        "name": "Bulbasaur",
        "type": ["Grass", "Poison"],
        "total": 318,
        "hp": 45,
        "attack": 49,
        "defense": 49,
        "sp_atk": 65,
        "sp_def": 65,
        "speed": 45,
    }

    # definimos tambem um pokemon do tipo agua:
    water_type_pokemon = {
        "national_number": "007",
        "evolution": None,
        "name": "Squirtle",
        "type": ["Water"],
        "total": 314,
        "hp": 44,
        "attack": 48,
        "defense": 65,
        "sp_atk": 50,
        "sp_def": 64,
        "speed": 43,
    }

    pokemon_json_content = json.dumps({ "results": [grass_type_pokemon, water_type_pokemon] })

    #substituimos a funcao padrao do python open por mock_open, uma versao que se comporta de forma parecida, porem simulada
    with patch("builtins.open", mock_open(read_data=pokemon_json_content)):
        # repare que o nome do arquivo não é importante aqui
        # a esses parâmetros não utilizados damos o nome de dummies
        # como neste contexto alteramos o open pelo mock_open,
        # o argumento "dummy" poderia ser substituído por qualquer coisa, já que não será utilizado pela função
        assert retrieve_pokemons_by_type("Grass", "dummy") == [
            grass_type_pokemon
        ]


# criamos o contexto de um pokemon do tipo grama
# @pytest.fixture
# def grass_type_pokemon():
#     return {
#         "national_number": "001",
#         "evolution": None,
#         "name": "Bulbasaur",
#         "type": ["Grass", "Poison"],
#         "total": 318,
#         "hp": 45,
#         "attack": 49,
#         "defense": 49,
#         "sp_atk": 65,
#         "sp_def": 65,
#         "speed": 45,
#     }


# # criamos o contexto de um pokemon do tipo agua
# @pytest.fixture
# def water_type_pokemon():
#     return {
#         "national_number": "007",
#         "evolution": None,
#         "name": "Squirtle",
#         "type": ["Water"],
#         "total": 314,
#         "hp": 44,
#         "attack": 48,
#         "defense": 65,
#         "sp_atk": 50,
#         "sp_def": 64,
#         "speed": 43,
#     }


# def test_retrieve_pokemons_by_type(grass_type_pokemon, water_type_pokemon):
#     #criamos um arquivo em memoria que o seu conteudo sao os dois pokemons:
#     fake_file = StringIO(
#         json.dumps({"results": [grass_type_pokemon, water_type_pokemon]})
#     )

#     # quando pesquisamos por pokemons do tipo grama, o pokemon do tipo agua nao deve ser encontrado
#     assert grass_type_pokemon in retrieve_pokemons_by_type("Grass", fake_file)