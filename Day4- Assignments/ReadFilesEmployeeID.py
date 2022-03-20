# open EmployeeData file in read mode

file=open("EmployeeData.txt","r")
data=list(file.readlines())
print(data)

ch='y'
while ch=='y':
    Id=input("Enter the employee ID for searching employee details: ")
    isfound=False
    for d in data:
    
        d=d.split(",")
        if d[0]==Id:
            print("Employee Name:",d[1])
            print("Employee Salary:",d[2])
            isfound=True
            break
    
    if isfound==False:
        print("Employee not found in data")

    ch=input("Do you want to search other employee details (y/n) :")
    

file.close()

input()
