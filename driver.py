import hashlib
from AES import AESCipher
import numpy as np

def reg_phase():
	#TODO: Compare with auth data table

	DB=np.load('pass.npy').item()
	
	usr=input('Enter User Name: ')
	psw=input('Enter Password: ')
	hashed_pass=hashlib.sha256(psw.encode('ascii')).hexdigest()
	print(hashed_pass)

	aes = AESCipher('passwword')
	if usr not in DB.keys():
		print("Please Wait....")
		print("Authenticating...")
		print()
		DB[usr]=aes.encrypt(hashed_pass)
		print(DB)
		print()
		print(DB[usr])
		np.save('pass.npy', DB) 

	else:
		print("Username Already Exists.")
		print("Please Wait....")
		print("Validating...")
		print(DB[usr])
		print('\n\n')
		print(DB)
		print('\n\n')
		print(aes.decrypt(DB[usr]))
		if hashed_pass == aes.decrypt(DB[usr]):
			print('Login Successful')
		else:
			print('Invalid Credentials')
			reg_phase()


reg_phase()

	
