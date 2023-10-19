import requests

import pytest

host = 'https://api.pokemonbattle.me:9104'

def test_trainers_status_code():
    response = requests.get(f'{host}/trainers', params = {"level" : "1"})
    assert response.status_code == 200

@pytest.mark.parametrize('key,value', [("trainer_name", "Pushok"),
                                       ("city", "Tbilisi")])

def test_trainer_name_and_city(key, value):
    response = requests.get(f'{host}/trainers', params = {"trainer_id" : "2555"})
    assert  response.json()[key] == value 

