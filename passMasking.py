import sys

def encryption(password, key, upper_limit, low_limit):
	encrypted = []
	for msg in password:
	    formula_enc = ord(msg) + key
	    if formula_enc > upper_limit:
	        encrypted.append(chr((formula_enc % upper_limit) + low_limit))
	    else:
	        encrypted.append(chr(formula_enc % upper_limit))

	encrpyt = ''.join(encrypted)
	return encrpyt

def decryption(password, key, upper_limit, low_limit):
	decrypted = []
	for msg in password:
	    formula_dec = ord(msg) - key
	    if formula_dec < low_limit:
	        decrypted.append(chr((formula_dec - low_limit) % upper_limit))
	    else:
	        decrypted.append(chr((formula_dec) % upper_limit))

	decrypt = ''.join(decrypted)
	return decrypt

def switch(option, password, key, upper_limit, low_limit):
	if option == "-e":
		return encryption(password, key, upper_limit, low_limit)
	elif option == "-d":
		return decryption(password, key, upper_limit, low_limit)
	elif option in ("-h", "--help"):
		return "==========Script Usage==============\n\n  passMasking.py [-e|-d] [\"password\"]\n\n  -e -> for encryption password \n  -d -> for decryption password\n\n"
	else:
		return "==========Script Usage==============\n\n  passMasking.py [-e|-d] [\"password\"]\n\n  -e -> for encryption password \n  -d -> for decryption password\n\n"


if __name__ == "__main__":
	option = sys.argv[1]
	if len(sys.argv) < 3:
		password = ""
	else:
		password = sys.argv[2]
	key = len(password)
	upper_limit = 127
	low_limit = 33
	print(switch(option, password, key, upper_limit, low_limit))