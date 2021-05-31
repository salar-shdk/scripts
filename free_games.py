#!/usr/bin/env python
import requests
import json
import notify2
from datetime import datetime

STORES = ['steam'] # steam, epic, humble, itch
URL = 'https://claimfreegames.com/feed.json'

data = json.loads(requests.get(URL).text)['games']

notify2.init('free games')

for game in data:
    if game['market'] in STORES:
        title = game['title']
        date = datetime.strptime(game['sale_end'].split('.')[0], '%Y-%m-%dT%H:%M:%S')
        n = notify2.Notification(f'{title} | time left: {date - datetime.now()}')
        n.show()
