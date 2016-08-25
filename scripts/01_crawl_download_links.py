#!/bin/python
# -*- coding: utf-8 -*- 

import requests
import json
import sys
from bs4 import BeautifulSoup
import unshortenit

# Carregando JSON
with open("links.json") as infile:
    data = json.load(infile)

for post in data:
    soup = BeautifulSoup(requests.get(post['url']).text, "lxml")
    for post_body in soup.find_all("div", class_="post-body"):

        # Pegando link de download e desencurtando (se necessário)
        for anchor in post_body.find_all('a', href=True):
            if ("adf.ly" in anchor['href']):
                post["download_link"] = unshortenit.unshorten_only(anchor['href'])[0]
                break
            elif (("cloud.mail.ru" in anchor['href']) or ("mega.nz" in anchor['href'])):
                post["download_link"] = anchor['href']
                break

        # Printando estado atual das coisas
        print(json.dumps(post, sort_keys=True, indent=4))

with open('downloads.json', 'w') as fp:
    json.dump(data, fp)