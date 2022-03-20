# Find the factorial by function....

def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

print("Factorial of 5 is :",fact(5))
print("Factorial of 8 is :",fact(8))
print("Factorial of 10 is :",fact(10))
