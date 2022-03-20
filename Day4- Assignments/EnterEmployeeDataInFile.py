
ch="y"
while ch=="y":
    file=open("EmployeeData.txt","r")

    print("Enter New Employee details as below")
    Id=input("Enter Unique ID of employee: ")
    Name=input("Enter Employee name: ")
    Salary=input("Enter Employe Salary: ")

    data=list(file.readlines())
    Is=True
    for d in data:
        d=d.split(",")
        if d[0]==Id:
            print(Id,"already exist in employee data")
            Is=False
            file.close()
            break


    if Is:
        fileptr=open("EmployeeData.txt","a")
        fileptr.write(Id+","+Name+","+Salary+"\n")
        print("Employee details updated successfully")
        fileptr.close()

    ch=input("Do you want to Enter other employee data (y/n: ")
    
