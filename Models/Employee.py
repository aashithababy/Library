from Connection.database_connection import DBConnect

class Employee:
    def __init__(self, name, age, doj, created_on, is_active):
        self.name = name
        self.age = age
        self.doj = doj
        self.createdOn = created_on
        self.isActive = bool(int(is_active))  # Convert "1" or "0" to True/False

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Age: {self.age}")
        print(f"Employee Date of Joining: {self.doj}")
        print(f"Employee Created On: {self.createdOn}")
        print(f"Employee is Active: {self.isActive}")


class InputEmployeeDetails:
    def input_employee_details(self):
        name = input("Please insert Employee Name (characters only): ")
        age = input("Please insert Employee Age (integers only): ")
        doj = input("Please insert Date of Joining (Date format only): ")
        created_on = input("Please insert Date of Creation (Date format only): ")
        is_active = input("Please insert if the employee is Active or Not (1 or 0): ")
        return name, age, doj, created_on, is_active



input_details = InputEmployeeDetails()
name, age, doj, created_on, is_active = input_details.input_employee_details()


employee = Employee(name, age, doj, created_on, is_active)
employee.display()

db = DBConnect()
db.insert_employee(name, age, doj, created_on, is_active)
print("Employee details successfully inserted into the database!")

