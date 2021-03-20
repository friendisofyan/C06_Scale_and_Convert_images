#!/usr/bin/env python3

from PIL import Image
import os

os.chdir("images")
for file in os.listdir():
	if file != ".DS_Store":
		im = Image.open(file).convert("RGB")
#		print(im.format, im.size, im.mode)

		path,filename = os.path.split(file)
		filename = os.path.splitext(filename)[0]
		im.rotate(270).resize((128,128)).save("/opt/icons/{}.jpeg".format(filename))
	
print("done")
