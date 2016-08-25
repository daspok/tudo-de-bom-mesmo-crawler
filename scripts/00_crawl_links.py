#!/bin/python
# -*- coding: utf-8 -*- 

import requests
import json

# Armazena todos os links
all_posts = []
links = set()

# Relacionado ao website que desejo crawlear
label = "Narra%C3%A7%C3%A3o%20Humana"
fmt = "json"
max_results = 500
feed_url = "https://tudodebommermmo.blogspot.com.br/feeds/posts/default/-/{}?alt={}&max-results={}&orderby=updated".format(label, fmt, str(max_results))

# Primeira página do feed
r = requests.get(feed_url).json()
total_results = int(r['feed']['openSearch$totalResults']['$t'])
last_update = r['feed']['entry'][-1]['updated']['$t']

for entry in r['feed']['entry']:
	post = {
		"title": entry['title']["$t"],
		"url": entry['link'][-1]['href'],
		"tags": [x['term'] for x in entry['category']]
	}
	if (post['url'] not in links):
		links.add(post['url'])
		all_posts.append(post)
		print(post['url'])

# Demais páginas do feed
while (total_results != 1):
	r = requests.get(feed_url + "&updated-max={}".format(str(last_update))).json()
	
	for entry in r['feed']['entry']:
		post = {
			"title": entry['title']["$t"],
			"url": entry['link'][-1]['href'],
			"tags": [x['term'] for x in entry['category']]
		}
		if (post['url'] not in links):
			links.add(post['url'])
			all_posts.append(post)
			print(post['url'])

	last_update = r['feed']['entry'][-1]['updated']['$t']
	total_results = int(r['feed']['openSearch$totalResults']['$t'])

with open('links.json', 'w') as fp:
    json.dump(all_posts, fp)

print("Terminou!")
