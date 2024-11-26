import mysql.connector

class DBConnect:
    def __init__(self):
        # Connect to MySQL server and initialize database
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1986"
        )
        self.cursor = self.db_connection.cursor()

        # Create and use the database
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS Library_employee")
        self.cursor.execute("USE Library_employee")

        # Create employee table if not exists
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            employee_id INT AUTO_INCREMENT PRIMARY KEY,
            employee_name VARCHAR(30) NOT NULL,
            employee_age INT NOT NULL,
            doj DATE NOT NULL,
            createdOn DATE NOT NULL,
            isActive BOOLEAN
        )
        """)

    def insert_employee(self, name, age, doj, created_on, is_active):
        # Insert employee details into the database
        query = """
        INSERT INTO employee (employee_name, employee_age, doj, createdOn, isActive)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (name, age, doj, created_on, is_active))
        self.db_connection.commit()

