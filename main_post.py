import requests
import pprint

if __name__=='__main__':
    url='http://httpbin.org/post'
    payload = {
        'nombre':'Albin',
        'edad':'58'
    }
    header = {
        'content-type': 'application/json',
        'access-token': '43333333423421'
    }
    response = requests.post(url, json=payload, headers=header)
    if response.status_code == 200:
        #pprint.pprint(response.json()) 
        pprint.pprint(response.headers['Server'])