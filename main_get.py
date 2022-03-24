import requests
import pprint

if __name__=='__main__':
    url='http://httpbin.org/get'
    args = {
        'nombre':'Albin',
        'edad':'58'
    }
    response = requests.get(url, params=args)
    if response.status_code == 200:
        pprint.pprint(response.json()) 
        origin_json = response.json()['origin']  #como json es un diccionario podemos obtener cualquier valor del diccionario
        print(origin_json)