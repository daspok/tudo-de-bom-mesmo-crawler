#!/bin/python
# -*- coding: utf-8 -*- 

import requests
import json
import hashlib

# Carregando JSON
with open("downloads.json") as infile:
    data = json.load(infile)

for post in data:
    with open("output/" + hashlib.md5(post['title'].encode('utf-8')).hexdigest() + ".txt", 'w') as fp:
        fp.write(post['title'].encode('utf-8') + "\n")
        for tag in post['tags']:
            fp.write(tag.encode('utf-8') + ", ")
        fp.write("\n")
        fp.write(post['download_link'].encode('utf-8') + "\n")

