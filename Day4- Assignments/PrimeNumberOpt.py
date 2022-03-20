n=int(input("Enter the number: "))

isPrime=True

for i in range(2,n//2+1):
    if n%i==0:
        isPrime=False
        break

if isPrime:
    print("Prime Number")
else:
    print("Not Prime Number")

