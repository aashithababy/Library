from Connection.database_connection import DBConnect


class Library:
    def __init__(self):
        """
        Initialize the Library class with a database connection.
        """
        self.db = DBConnect()

    def read_employees(self):
        """
        Fetch all employees from the database.
        :return: List of employees or a message if none are found.
        """
        query = "SELECT id, name, age, doj, created_on, is_active FROM employees"
        employees = self.db.connection.execute(query).fetchall()
        if not employees:

            return "No employees found."
        result = []
        for emp in employees:
            result.append(
                f"ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}, DOJ: {emp[3]}, "
                f"Created On: {emp[4]}, Active: {'Yes' if emp[5] else 'No'}"
            )
        return result

    def update_employee(self, employee_id, name=None, age=None, doj=None):
        """
        Update an employee's details in the database.
        :param employee_id: The ID of the employee to update.
        :param name: (Optional) New name for the employee.
        :param age: (Optional) New age for the employee.
        :param doj: (Optional) New date of joining for the employee.
        :return: Update success message or error message.
        """
        # Check if the employee exists
        query = "SELECT id FROM employees WHERE id = ?"
        employee = self.db.connection.execute(query, (employee_id,)).fetchone()
        if not employee:
            return f"No employee found with ID {employee_id}."

        if name:
            self.db.connection.execute("UPDATE employees SET name = ? WHERE id = ?", (name, employee_id))
        if age:
            self.db.connection.execute("UPDATE employees SET age = ? WHERE id = ?", (age, employee_id))
        if doj:
            self.db.connection.execute("UPDATE employees SET doj = ? WHERE id = ?", (doj, employee_id))
        
        self.db.connection.commit()
        return f"Employee ID {employee_id} updated successfully."

    def delete_employee(self, employee_id):
        """
        Delete an employee from the database.
        :param employee_id: The ID of the employee to delete.
        :return: Deletion success message or error message.
        """
        # Check if the employee exists
        query = "SELECT id FROM employees WHERE id = ?"
        employee = self.db.connection.execute(query, (employee_id,)).fetchone()
        if not employee:
            return f"No employee found with ID {employee_id}."

        # Delete the employee
        self.db.connection.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
        self.db.connection.commit()
        return f"Employee ID {employee_id} deleted successfully."


# # Optional: Example usage for testing
# if __name__ == "__main__":
#     library = Library()
    
#     # Example: Reading employees
#     print("All Employees:")
#     print(library.read_employees())
    
#     # Example: Updating an employee
#     print(library.update_employee(1, name="John Doe", age=30))
    
#     # Example: Deleting an employee
#     print(library.delete_employee(1))
