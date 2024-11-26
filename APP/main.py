import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Library.Library import library

def main():
    lib = library()
    while True:
        print("\n\t 1.Add Employee\n ")
        print("\t 2.List Employee\n")
        print("\t 3.Update Employee\n")
        print("\t 4.Delete Employee\n")
        print("\t 5.Good Bye")
        choice=input("Enter your choice: ")

        if choice==1:
            lib.create_employee
        elif choice==2:
            lib.read_employees
        elif choice==3:
            lib.update_employee
        elif choice==4:
            lib.delete_employee
        elif choice==5:
            break;
        else:
            print("Invalid Choice")

if __name__=="__main__":
    main()