import sys

q = int(sys.stdin.readline().strip())

for i in range(1,q+1):
	if(i == 1):
		print(" "*(q-i)+"* ")

	elif(i==q):
		print("*"*(2*q-1))
	else:
		print(" "*(q-i)+"* "+" "*(2*i-4)+"*")

