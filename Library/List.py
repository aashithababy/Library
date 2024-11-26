import is_valid_name, is_valid_age, is_valid_doj
import Employee

class Library:
    def __init__(self):
        """Initialize an empty employee repository."""
        self.employees = {}

    def create_employee(self, name, age, doj):
        """Add a new employee to the repository."""
        employee_id = len(self.employees) + 1
        employee = Employee(name, age, doj)
        self.employees[employee_id] = employee
        return f"Employee {name} added with ID {employee_id}."

    def read_employees(self):
        """List all employees."""
        if not self.employees:
            return "No employees found."
        return [f"ID: {eid}, {emp}" for eid, emp in self.employees.items()]

    def update_employee(self, employee_id, name=None, age=None, doj=None):
        """Update an existing employee's details."""
        if employee_id not in self.employees:
            return f"No employee found with ID {employee_id}."
        employee = self.employees[employee_id]
        if name:
            employee.name = name
        if age:
            employee.age = age
        if doj:
            employee.doj = doj
        return f"Employee ID {employee_id} updated successfully."

    def delete_employee(self, employee_id):
        """Remove an employee from the repository."""
        if employee_id not in self.employees:
            return f"No employee found with ID {employee_id}."
        del self.employees[employee_id]
        return f"Employee ID {employee_id} deleted successfully."