from Library.List import Library

class main:
    while True:
        print("\n\t 1.Add Employee\n ")
        print("\t 2.List Employee\n")
        print("\t 3.Update Employee\n")
        print("\t 4.Delete Employee\n")
        choice=input("Enter your choice: ")

        if choice==1:
            Library.create_employee
        elif choice==2:
            Library.read_employees
        elif choice==3:
            Library.update_employee
        elif choice==4:
            Library.delete_employee
        