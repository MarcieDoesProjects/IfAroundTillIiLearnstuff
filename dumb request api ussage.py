#see how and where to get api
import requests
Insert_Name = input("whats your fav pokemon?:")
baseUrl = "https://pokeapi.co/api/v2"

requests.get(baseUrl)

def get_poki_info(name):
    pass
    url=f"{baseUrl}/pokemon/{name}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        print(f"pokedex found your pokemon!!")
        Poke_data = response.json()
        return Poke_data
        print(f"heres your data {Poke_data}")
    else:
        print(f"pokedex failed to retrieve PokeData { response.status_code}")
poke_name= f"{Insert_Name}"
poke_info = get_poki_info(poke_name)


if poke_info:
    print(f"name: {poke_info["name"].capitalize()}")
    print(f"ID: {poke_info["id"]}")
    print(f"height: {poke_info["height"]}")
    print(f"weight: {poke_info["weight"]}")
