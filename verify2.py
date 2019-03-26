from utils import comp

hashP=['0','0','0','0']
np=[['0','0','*',
'0'],['0','*','0','1'],['1','*','0','0'],['1','0','*','0'],['0','*','0','1']]
flag=False
m=len(hashP)

def main():

	for i in range(m):
		# print(number_of_sp(np[i]))
		if number_of_sp(np[i])!=3 :
			return True
	# print(number_of_ds(np[m-1],np[m]))
	if number_of_ds(np[m-1],np[m])!=1 or number_of_ds(np[m+1],np[m+2])!=1 or number_of_ds(np[m+3],np[m+4])!=1 :
		return False
	else :
		np[m-1]=merge(np[m-1],np[m])
		np[m+1]=merge(np[m+1],np[m+2])
		np[m+3]=merge(np[m+3],np[m+4])

	if number_of_ds(np[m+1],np[m+3])!= 1 :
		return False
	else :
		np[m]=merge(np[m+1],np[m+3])

	for i in range(m-1,-1,-1):
		if number_of_sp(np[i])!=1 :
			return False

		k=index_of_sp(np[i])
		x[k]=comp(to_bit(np[i][k]))
		for j in range(i-2,-1,-1):
			if np[j][k]!=to_symbol(x[k]) or np[j][k]!='*' :
				return False

			np[j][k]='*'


	if x==hashP:
		return True
	else :
		return False

def to_bit(x):
	if type(x)==type('a'):
		return int(x)
	else :
		return x

def to_symbol(b):
	if type(b) == type('a'):
		return b
	else:
		return str(b)

def index_of_sp(x):
	for i in range(len(x)):
		if x[i]!='*':
			return (i)

def number_of_sp(x):
	count=0
	for i in range(len(x)):
		if x[i]=='*':
			count+=1
	return (len(x)-count)

def number_of_ds(a,b):
	count=0
	for i in range(len(a)):
		if a[i]!=b[i] :
			count+=1
	return count

def merge(a,b):
	for i in range(len(a)):
		if a[i]!=b[i] :
			a[i]='*'
	return a

print(main())