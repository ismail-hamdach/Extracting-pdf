import json
from bs4 import BeautifulSoup
import requests

qsts = []

with open('text.html', 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')
    Questions = soup.find_all('div', {'id': 'Question'})
    for qs in Questions:
        qst = dict()
        qst['q'] = ''
        qst['rep'] = []
        for index, span in enumerate(qs.find_all("span")):
            if index == 0:
                qst['q'] = span.text
            else:
                qst['rep'].append(span.text)
        qsts.append(qst)

with open('html.json', 'w') as file:
    file.write(json.dumps(qsts, separators=(',', ':')))
