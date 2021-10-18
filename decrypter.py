import os

filename = input('Which file do you want to en- or decrypt?\n')
en_or_de = input('Encrypt or decrypt that file?\nen/de\n')
if en_or_de == 'de':
	key = input('Which key do you want to use?\n')

def encrypt(filename):
    zu_verschluesseln = open(filename, "rb").read()
    size = len(zu_verschluesseln)
    key = os.urandom(size)
    with open(filename +'.key', 'wb') as key_out:
        key_out.write(key)
    verschluesselt = bytes(a ^ b for (a,b) in zip(zu_verschluesseln, key))
    with open(filename, "wb") as encrypted_out:
        encrypted_out.write(verschluesselt)

def decrypt(filename,key):
    file = open(filename, 'rb').read()
    key = open(key, 'rb').read()
    entschluesselt = bytes(a ^ b for (a,b) in zip(file, key))
    with open(filename, 'wb') as decrypted_out:
        decrypted_out.write(entschluesselt)
if en_or_de == 'en':
	try:
		encrypt(filename)
	except:
		print('Wrong Filename')
elif en_or_de == 'de':
	try:
		decrypt(filename,key)
	except: 
		print('Wrong key')
else: 
	print('wrong input')
