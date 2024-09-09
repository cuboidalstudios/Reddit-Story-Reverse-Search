from bs4 import BeautifulSoup
import requests

import common


def redditSearch(query):
    query = query[0:50]
    url = 'https://www.google.com/search'

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
    }
    parameters = {'q': query}

    content = requests.get(url, headers=headers, params=parameters).text
    soup = BeautifulSoup(content, 'html.parser')

    search = soup.find(id='search')

    link = search.find('a')
    link = link.get('href')
    print(link)
    common.changeLink(link)
