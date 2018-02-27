import sys
import array

q = int(sys.stdin.readline().strip())

def one_make_dp(x):
#bottom - up
	D = []
	D.append(0)
	D.append(0)	
	
	for i in range(2,x+1):
		#print("-"*10,i,"-"*10)
		temp= []
		if i%2 == 0:
			temp.append(D[i//2])
			#print(2,temp)
		
		if i%3 == 0:
			temp.append(D[i//3])
			#print(3,temp)
		
		temp.append(D[i-1])
		#print(-1,temp)
		
		D.append(min(temp)+1)
		#print(5,D)

	return D[x]



memo = [None]*(q+1)

def one_make_recur(x):

	if(x==1):
		memo[x]=0
		return memo[x]

	if memo[x] is not None:
		return memo[x]

	memo[x] = one_make_recur(x-1)

	if x%2 == 0:
		memo[x]= min(one_make_recur(x//2),memo[x])

	if x%3 == 0:
		memo[x]= min(one_make_recur(x//3),memo[x])
		
	memo[x] = memo[x]+1

	return(memo[x])

print(one_make_recur(q))