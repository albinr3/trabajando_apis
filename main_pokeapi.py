import requests
import pprint

if __name__=='__main__':
    url='https://pokeapi.co/api/v2/pokemon-form'
    args = {"limit": 2000} #este parametro es lo que te ayuda a elegir cuantos pokemon quieres mostrar
    response = requests.get(url, params=args)
    print(response.url)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get("results", [])
        if results != []:
            index = 0
            for pokemon in results:
                index += 1
                print(str(index) + "-" + pokemon["name"])
       