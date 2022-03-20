
def Factorial(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

def nPr(n,r):
    return (Factorial(n)//Factorial(n-r))

def nCr(n,r):
    return Factorial(n)//(Factorial(n-r)*Factorial(r))

n=int(input("Enter the value of n: "))
r=int(input("Enter the value of r: "))

print("nPr =",nPr(n,r))
print("nCr =",nCr(n,r))

input()
