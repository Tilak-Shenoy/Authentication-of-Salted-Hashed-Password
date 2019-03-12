import numpy as np
from utils import create_sequence_of_symbol, to_symbol,inv_permute,comp, permute
# from AES import encrypt
import hashlib
import random


def prefix(s):
	ndb=[]
	perm_bits=permute(s)
	# perm_bits=shuffle_forward(s)
	# print(perm_bits)
	# print("Hellp")
	m=len(perm_bits)
	# j_ind=[i for i in range(len(s))]
	# k_ind=[_ for _ in range(len(s))]

	for i in range(m-1,1,-1):

		x=list(create_sequence_of_symbol(m))
		# print(x)
		# for j in range(i-1):
		# 	x[j]=to_symbol(perm_bits[j])

		# x[i]= to_symbol(comp(perm_bits[i]))
		# for j in range(i+1,m):
		# 	x[j]='*'

		# print((x))
		# ndb.append(inv_permute(x))
		# ndb.append(x)

		x[i]=to_symbol(comp(perm_bits[i]))
		j=random.randint(0,i-1)
		while True:
			k=random.randint(0,i-1)
			if j!=k:
				break
		x[j]=to_symbol(perm_bits[j])
		x[k]=to_symbol(perm_bits[k])
		# print(inv_permute(x))
		print('\n\n')
		ndb.append(inv_permute(x))

	x=list(create_sequence_of_symbol(m))
	x[0]=to_symbol(perm_bits[0])
	x[1]=to_symbol(comp(perm_bits[1]))
	j=random.randint(2,m-1)
	x[j]='0'
	ndb.append(inv_permute(x))
	x[j]='1'
	ndb.append(inv_permute(x))

	x=list(create_sequence_of_symbol(m))
	x[0]=to_symbol(comp(perm_bits[0]))
	j=random.randint(1,m-1)
	while True:
		k=random.randint(1,m-1)
		if j!=k:
			break
	x[j]='0'
	x[k]='0'
	ndb.append(inv_permute(x))
	x[k]='1'
	ndb.append(inv_permute(x))
	x[k]='*'
	# ndb.append(inv_permute(x))
	while True:
		k=random.randint(1,m-1)	
		if j != k:
			break
	x[j]='1'
	x[k]='0'
	ndb.append(inv_permute(x))
	x[k]='1'
	ndb.append(inv_permute(x))



	return ndb


def reg_phase(paswd):
	#TODO: Compare with auth data table

	hashed_pass=hashlib.sha256(paswd.encode('ascii')).hexdigest()
	bin_hashed_pass="{0:b}".format(int(hashed_pass,16))
	NDB=prefix(list(bin_hashed_pass))

print(prefix([0,0,0,0]))