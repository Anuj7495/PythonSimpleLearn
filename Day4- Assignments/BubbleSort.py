data=[21,356,5,4,98,17,25,61,14,19,92,3,7,84,56,17]
n=len(data)

for i in range(n,0,-1):
    for j in range(0,i-1):
        if (data[j]>data[j+1]):
            temp=data[j]
            data[j]=data[j+1]
            data[j+1]=temp

print(data)
