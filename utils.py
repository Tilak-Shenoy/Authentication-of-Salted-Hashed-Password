# Generate sequence of '*' of length m
def create_sequence_of_symbol(m):
	sym=''
	for i in range(m):
		sym+='*'
	return sym

def to_symbol(b):
	if type(b) == type('a'):
		return b
	else:
		return str(b)


def permute(arr):
	table=[2,3,4,1]
	arr2=[]
	for i in range(len(arr)):
		arr2.append(arr[table[i]-1])
	return arr2

def inv_permute(arr) : 
	table = [4,1,2,3]
	arr2=[]
	for i in range(len(arr)):
		arr2.append(arr[table[i]-1])
	return arr2

def comp(b):
	if b==0:
		return 1
	elif b==1:
		return 0
	else:
		print('Error: Undefined bit value ',b)
		return None
 
