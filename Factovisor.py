
import math
n,m=map(int,input().split())
n_fact=math.factorial(n)
if n_fact%m==0:
    print(m,"divides",n,"!")
else:
    print(m,"does not divides",n,"!")
