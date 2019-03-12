hashP=input("The hashed password")
np=[]
flag=False
m=len(hashP)

for i in range(m):
	if (number_of_specified_position(np[i])!=i):
		flag=False

for i in range(m):
	if (number_of_specified_position(np[i])!=1):
		flag=False
	k=index_sp(np[i])
	x[k]=to_bit(np[i][k])
	j=i+1
	for j in range(m):
		if (np[j][k]!=to_symbol(x[k])):
			flag=False
		np[j][k]='*'
if (x==hashP):
	flag=True
else:
	flag=False




def to_bit(x):
	return n

def to_symbol(x):
	return n


def index_sp(x):

	return m


def number_of_specified_position(x):
	count=0
	arr=map(int,str(x))
	for i in range(len(arr)):
		if arr[i]=='*':
			count++
	return (len(arr)-count)