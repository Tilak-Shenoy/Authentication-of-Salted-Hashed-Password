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

# if element 4 is at position 3 in an array, then in reverse permutation, 
# we insert 3 (position of element 4 in the array) in position 4 (element value).
def inv_permute(arr) : 
	# arr2 = [0] *(len(arr)) 
	table = [4,1,2,3]
	arr2=[]
	for i in range(len(arr)):
		arr2.append(arr[table[i]-1])
	return arr2

	# Inserting position at their 
	# respective element in second array 
	# for i in range(len(arr)-1) : 
	# 	if arr[i] != '*':
	# 		# print(arr[i])
	# 		arr2[int(arr[i])%len(arr)] = arr[i]
	# 	else:
	# 		arr2[i]='*'
	# return arr2

def comp(b):
	if b==0:
		return 1
	elif b==1:
		return 0
	else:
		print('Error: Undefined bit value ',b)
		return None

# print(inv_permute([0,0,0,0]))	  
