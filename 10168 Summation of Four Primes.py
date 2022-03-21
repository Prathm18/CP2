import math;
def isPrime(x):
    s = int(math.sqrt(x))
    for i in range(2,s+1):
        if (x % i == 0):
            return 0
    return 1
def Num(x):
    ab=[0]*2
    for i in range(2,int(x / 2)+1):
        if (isPrime(i) != 0 and isPrime(x - i) != 0):
            ab[0] = i
            ab[1] = x - i
            return ab
def generate(n):
    if(n <= 7):
        print("Impossible to form")
    if (n % 2 != 0):
        ab=Num(n - 5)
        print("2 3",ab[0],ab[1])
    else:
        ab=Num(n - 4)
        print("2 2",ab[0],ab[1])
 

if __name__=='__main__':
    n = int(input())
    generate(n)
