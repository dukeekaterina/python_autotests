import requests

token = "..."

'''response_kill = requests.post('https://api.pokemonbattle.me:9104/pokemons/kill', 
                                json = {"pokemon_id": "12724"}, 
headers = {"Content-Type" : "application/json", "trainer_token" : token,})

print(response_kill.text)'''

response_create = requests.post('https://api.pokemonbattle.me:9104/pokemons', 
                                json = {"name": "generate",
                                        "photo": "generate"}, 
headers = {"Content-Type" : "application/json", "trainer_token" : token,})

print(response_create.text)


response_id = requests.get('https://api.pokemonbattle.me:9104/pokemons', params =  {"trainer_id" : "2555"}, 
                           headers = {"Content-Type" : "application/json", "trainer_token" : token,})

print(response_id.text)

my_pokemons = response_id.json()

pokemon_id = my_pokemons[0]["id"]

response_name = requests.put('https://api.pokemonbattle.me:9104/pokemons', 
                             json = {"pokemon_id": pokemon_id,
                                     "name": "Peps",
                                     "photo": "https://dolnikov.ru/pokemons/albums/008.png"}, 
headers = {"Content-Type" : "application/json", "trainer_token" : token,})

print(response_name.text)

response_add_pokeball = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
                                      json = {"pokemon_id": pokemon_id}, 
headers = {"Content-Type" : "application/json", "trainer_token" : token})

print(response_add_pokeball.text)

