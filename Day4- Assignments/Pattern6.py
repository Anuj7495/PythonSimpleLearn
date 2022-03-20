n=int(input("Enter the value of n : "))

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")

    for j in range(1,2*i):
        print("*",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i+1,1,-1):
        print(" ",end="")

    for j in range(2*i,1,-1):
        print("*",end="")
    print()

input()
    
