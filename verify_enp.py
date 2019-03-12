hashP=input("The hashed password")
np=[]
flag=False
m=len(hashP)

def main():

	for i in range(m):
		if (number_of_specified_position(np[i])!=i):
			return False

	for i in range(m):
		if (number_of_specified_position(np[i])!=1):
			return False
		k=index_sp(np[i])
		x[k]=(~to_bit(np[i][k]))
		j=i+1
		for j in range(m):
			if (np[j][k]!=to_symbol(x[k])):
				return False
			np[j][k]='*'
	if (x==hashP):
		return True
	else:
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

def index_sp(x):
	arr=list(map(int,str(x)))
	for i in range(len(arr)):
		if arr[i]!='*':
			return (i+1)

def number_of_specified_position(x):
	count=0
	arr=list(map(int,str(x)))
	for i in range(len(arr)):
		if arr[i]=='*':
			count++
	return (len(arr)-count)