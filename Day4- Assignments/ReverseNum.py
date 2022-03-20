n=int(input("Enter the number: "))

ans=0

while n>0:
    r=n%10
    n//=10
    ans=ans*10+r

print("Reverse of given number is :",ans)
    
    
input()
