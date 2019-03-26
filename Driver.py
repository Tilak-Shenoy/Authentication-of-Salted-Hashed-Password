import hashlib
import random
from AES import AESCipher

def Driver():
	usr=input('Enter User Name: ')
	psw=input('Enter Password: ')
	hashed_pass=hashlib.sha256(psw.encode('ascii')).hexdigest()
	print(len(hashed_pass))
	salt=[]
	for _ in range(3):
		while True:
			x=random.getrandbits(48)
			bin_x="{0:b}".format(int(x))
			if bin_x not in salt and len(bin_x)==48:
				break
		salt.append(bin_x)

	while True:
		y=random.getrandbits(112)
		bin_y="{0:b}".format(int(y))
		if len(bin_y)==112:
			break
	salt.append(bin_y)

	bin_hashed_pass="{0:b}".format(int(hashed_pass,16))
	len(bin_hashed_pass)
	if len(bin_hashed_pass) != 256:
		bin_hashed_pass=list(bin_hashed_pass)
		for i in range(256-len(bin_hashed_pass)):
			bin_hashed_pass.append('0')
	
		bin_hashed_pass=''.join(bin_hashed_pass)
	print(len(bin_hashed_pass))
	print(type(bin_hashed_pass))

	b3=bin_hashed_pass[:80]+salt[0]
	b4=bin_hashed_pass[80:160]+salt[1]
	b1=bin_hashed_pass[160:240]+salt[2]
	b2=bin_hashed_pass[240:]+salt[3]
	print(len(salt[0]),len(salt[1]),len(salt[2]),len(salt[3]))
	print(len(b1),len(b2),len(b3),len(b4))
	# print(len(bin_hashed_pass[240:]))


	aes=AESCipher('pass')
	c1=aes.encrypt(b1)
	print((c1))
	print(len(c1))
	print(type(c1))
	# if len(c1) != 256:
	# 	c1=list(c1)
	# 	for i in range(256-len(c1)):
	# 		c1.append(0)
	
	# c1=bytes(c1)
	
Driver()

