import numpy as np
from utils import create_sequence_of_symbol, to_symbol,inv_permute
# from permute import shuffle_forward, shuffle_backward


def prefix(s):
	ndb=[]
	perm_bits=np.random.permutation(s)
	# perm_bits=shuffle_forward(s)
	# print(perm_bits)
	m=len(perm_bits)

	for i in range(m):

		x=list(create_sequence_of_symbol(m))
		# print(x)
		for j in range(1,i-1):
			x[j]=to_symbol(perm_bits[j])

		x[i]= to_symbol(~perm_bits[i])
		for j in range(i+1,m):
			x[j]='*'

		# print(inv_permute(x))
		ndb.append(inv_permute(x))

	return ndb

s=[2,3,0,4,1]
print(prefix(s))