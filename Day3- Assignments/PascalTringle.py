def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

def nCr(n,r):
    return fact(n)//(fact(n-r)*fact(r))

n=int(input("Enter the value of n as upto n quotients : "))

for i in range(0,n+1):
    for j in range(0,i+1):
        print(nCr(i,j),end=" ")
    print()


input()
        
