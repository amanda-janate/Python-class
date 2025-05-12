'''web scraping'''
import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3333/'
response = requests.get(url)

# print(response)
# print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.text)

raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

if parsed_html.title is not None:
    print(parsed_html.title.text)

lorem = parsed_html.select_one('#intro > div > h2')
if lorem is not None:
    print(lorem.text)
    parent = lorem.parent
    if parent is not None:
        # print(parent)
        for p in parent.select('p'):
            print(p.text)
