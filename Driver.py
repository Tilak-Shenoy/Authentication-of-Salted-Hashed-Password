import hashlib
import random
from AES import AESCipher
import secrets
import json
import time

def Driver():
	with open('pass.json','r') as f:
		data=json.load(f)
		# print(data)

	f.close()


	with open('salt.json','r') as f1:
		salt_data=json.load(f1)
	# 	print(salt_data)

	f1.close()

	# Uncomment the below line during the first run
	# data={'authT':[]}
	# salt_data={'salts':[]}
	usr=input('Enter User Name: ')
	psw=input('Enter Password: ')
	start_time = time.time()
	hashed_pass=hashlib.sha256(psw.encode('ascii')).hexdigest()
	print(len(hashed_pass))

	user=[]
	for u in data['authT'].items():
		print(u[0])
		user.append(u[0])

	print('------------Users-----------')
	print(user)
	print('----------------------------')


	salts=[]
	flag=False
	if usr in user:
		salts=salt_data['salts'][usr]
		print('------------Salts-----------')
		print(salts)
		flag=True
	else:
		for _ in range(3):
			while True:
				x=secrets.token_hex(6)

				if x not in salts: 
					break
			salts.append(x)

		while True:
			y=secrets.token_hex(14)
			if y not in salts:
				break
		salts.append(y)

	print('Hash Length: ', len(hashed_pass))
	b3=hashed_pass[:20]+salts[0]
	b4=hashed_pass[20:40]+salts[1]
	b1=hashed_pass[40:60]+salts[2]
	b2=hashed_pass[60:]+salts[3]

	int_b2=int(b2,16)
	int_b3=int(b3,16)
	int_b4=int(b4,16)
	print('Salt length: ',len(salts[0]),len(salts[1]),len(salts[2]),len(salts[3]))
	# print(len(b1),len(b2),len(b3),len(b4))


	aes=AESCipher('pass')
	c1=aes.encrypt(b1)
	print('c1: ',(c1.hex()))
	# print(len(c1.hex()))
	int_c1=int(c1.hex()[:32],16)
	b2_part="{:x}".format(int_c1^int(int_b2))

	# print(len(b2_part))

	c2=aes.encrypt(b2_part)
	print('c2: ',c2.hex())
	int_c2=int(c2.hex()[:32],16)
	b3_part = "{:x}".format(int_c2^int(int_b3))

	c3=aes.encrypt(b3_part)
	print('c3: ',c3.hex())
	int_c3=int(c3.hex()[:32],16)
	b4_part="{:x}".format(int_c3^int_b4)

	c4=aes.encrypt(b4_part)
	print('c4: ',c4.hex())

	if flag:
		if c2.hex()==data['authT'][usr][0] and c4.hex()== data['authT'][usr][1]:
			print('Auth Success')
		else:
			print('Auth Failed')
	else:
		pswd=[c2.hex(),c4.hex()]

		data['authT'][usr]=pswd
		salt_data['salts'][usr]=salts

		with open('pass.json','w') as fp:
			json.dump(data,fp)

		fp.close()
		with open('salt.json','w') as sp:
			json.dump(salt_data,sp)
		sp.close()
		print('Password Saved')

	end_time=time.time()

	print('Time Taken= ',end_time-start_time)
	
Driver()

