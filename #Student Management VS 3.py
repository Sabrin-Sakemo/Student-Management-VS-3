#Student Management VS 3
#Author:Sabrin Nahar
#Date:22.07.2026

while True:
    print ("1.Add Student")
    print("2.Show Student List")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.Total Number of Student")
    print("6.Exit")

    try:
        choice=int(input("Choice:"))
    except ValueError:
        print("Invalid choice. Please Enter Right One")
        continue
    if choice==1:
        try:
            add_stu=input("Student Name:")
            if not add_stu:
                print("Student Name Can't Empty")
            else:
                with open("student_data.txt", "a") as f_name:
                    f_name.write(add_stu+",")                   
        except:
            print("Please Enter Valid Name")
        try:
            stu_id=input("Student ID:")
            with open("student_data.txt", "a") as f_name:
                    f_name.write(stu_id +",")   
        except:
            print("Please Enter Valid ID")
        try:
            section=input("Enter Section:")
            if section== "A" or section == "B":
                with open("student_data.txt", "a") as f_name:
                    f_name.write(section + "\n") 
                    print("Sucessfully Added")
            else:
                print("Please Enter Section A or B")
        except:
            print ("Wrong section. PLease Enter Valid One.")
        
    if choice==2:
        with open("student_data.txt") as f_name:
            stu_list=f_name.read()
            if stu_list=="":
                print("No Student Found")
            else:
                print(stu_list)
    if choice ==3:
        search=input("Enter Student Name:").strip().lower()
        found=False
        with open ("student_data.txt") as f_name:
            for s_stu in f_name:
                data=s_stu.strip().split(",")
                dada=data[0].lower()
                if search in dada:
                    found=True
                    print("Student Name:",data[0])
                    print("Student Id:",data[1])
                    print("Student Section:", data[2])
                    break
        if not found:
            print ("Not Found,",search,"Add First.")

    if choice==4:
        del_stu=input("Student Name:").strip().lower()
        found=False
        student=[]
        with open("student_data.txt")as f_name:
            dada=f_name.readlines()
        for new_stu in dada:
            data=new_stu.split(",")
            name=data[0]
            if data[0].lower().strip()==del_stu:
                found=True
            else:
                student.append(new_stu)
        with open("student_data.txt","w")as f_name:
            f_name.writelines(student)
        if found:
                print ("Successfully Deleted")
                continue
        else:
                print("Student Not found")
                continue
    if choice==5:
        with open("student_data.txt") as f_name:
            tol=f_name.readlines()
        print("Total Number of students is:",len(tol))
    if choice==6:
     print("Thank you for using")
     break



            

            

    
            




