from time import sleep

import requests
import json
from bs4 import BeautifulSoup
from classes import Imigrante


requests.packages.urllib3.disable_warnings() # noqa

url = ''
headers = {
    'Accept': '*/*',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': '',
    'DNT': '1',
    'Origin': '',
    'Referer': '',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}

for i in range(63675):
    data = {
        'nmgp_opcao': 'ajax_navigate',
        'script_case_init': '1',
        'script_case_session': 'qpa9tcag3gra4petvdadc52cs6',
        'opc': 'rec',
        'parm': '{}'.format(i+1),
    }

    response = requests.post(url, headers=headers, data=data, verify=False)
    content_page = json.loads(response.text)['setValue'][1]['value']
    soup = BeautifulSoup(content_page, 'html.parser')

    imigrante = Imigrante(soup, i+1)
    imigrante.save()


