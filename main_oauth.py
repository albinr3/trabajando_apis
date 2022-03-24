import requests
import pprint
client_id= "8f4df31058da37c6653c"
cliente_secret= "a15e7accac3334ede15bc89196b54e3f4ea1945d"
code='16832ccea6c7428a025c'
access_token= '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'

if __name__=='__main__':
    
    url='https://github.com/login/oauth/access_token'
    payload= {
        "client_id":client_id,
        "client_secret":cliente_secret,
        "code":code
    }
    header = {"Accept": "application/json"}
    response = requests.post(url, json=payload, headers=header)
    print(response.json())
    