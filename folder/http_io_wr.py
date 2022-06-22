import requests
from requests.exceptions import HTTPError
import pandas as pd

rand_url = []
rand_url.append(input('input url:\n')) 
tables = pd.read_html(str(rand_url))
print(tables[0])


for url in rand_url:
    try:
        response = requests.get(url)
 
        # если ответ успешен, исключения задействованы не будут
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    except url.status_code == 404 as err404:
        print(f'Not Found.: {err404}')
    else:
        print('Success!')
        
