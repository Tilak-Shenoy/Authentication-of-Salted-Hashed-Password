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

# if element 4 is at position 3 in an array, then in reverse permutation, 
# we insert 3 (position of element 4 in the array) in position 4 (element value).
def inv_permute(arr) : 
	arr2 = [0] *(len(arr)) 
	  
	# Inserting position at their 
	# respective element in second array 
	for i in range(0, len(arr)) : 
		if arr[i] != '*':
			# print(arr[i])
			arr2[int(arr[i])%len(arr)] = i + 1
		else:
			arr2[i]='*'

	return arr2
	  
