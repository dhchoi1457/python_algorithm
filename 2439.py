import sys

in_number = int(sys.stdin.readline().strip())
for i in range(1,in_number+1):
	print(" "*(in_number-i) +  "*"*i)