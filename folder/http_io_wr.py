"""
import requests
#get we can include in var
g = requests.get('https://api.github.com')
if g.status_code == 200:
    print('Success!')
elif g.status_code == 404:
    print('Not Found.')
print(g.status_code)
"""

import requests
from requests.exceptions import HTTPError

rand_url = []
rand_url.append(input()) 

for url in rand_url:
    try:
        response = requests.get(url)
 
        # если ответ успешен, исключения задействованы не будут
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
       # url = str(rand_url)
        #r = requests.get(url)
        #with open('test.html', 'w') as output_file:
         #   output_file.write(r.text.encode('cp1251'))
