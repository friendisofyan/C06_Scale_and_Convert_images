#! /usr/bin/env python3

import os
import requests

dir = "/data/feedback/"
for file in os.listdir(dir):
	key = ["title","name","date","feedback"]
	content = {}

	with open (dir+file, "r") as txtfile:
		key_index = 0;
		for line in txtfile:
			line = line.replace("\n","")
			content[key[key_index]] = line.strip("\n")
			key_index += 1
#	print("Sedang meng edit file ke :"+file)
	
	response = requests.post("http://34.66.213.76/feedback/", json=content)
	response.raise_for_status()
	print("selesai upload file ke :"+file)


