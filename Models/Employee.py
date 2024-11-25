class Employee:
    def __init__(self,name,age,doj,createdOn,isActive):
        self.name=name
        self.age=age
        self.doj=doj
        self.createdOn=createdOn
        self.isActive=isActive

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Age: {self.age}")
        print(f"Employee Date of Joining : {self.doj}")
        print(f"Employee Created On: {self.createdOn}")
        print(f"Employee is Active or not: {self.isActive}")
    
    