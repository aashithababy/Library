import re
from datetime import datetime


class Validation:
    def is_valid_name(name):
        """
        Validate that the name contains only alphabetic characters and spaces.
        :param name: The name to validate.
        :return: True if valid, False otherwise.
        """
        if not name or not re.match(r"^[A-Za-z\s]+$", name):
            return False
        return True


    def is_valid_age(age):
        """
        Validate that the age is a positive integer and within a reasonable range.
        :param age: The age to validate.
        :return: True if valid, False otherwise.
        """
        try:
            age = int(age)
            return 18 <= age <= 65
        except ValueError:
            return False


    def is_valid_doj(doj):
        """
        Validate the date of joining format (YYYY-MM-DD) and ensure it is not in the future.
        :param doj: The date of joining to validate.
        :return: True if valid, False otherwise.
        """
        try:
            date = datetime.strptime(doj, "%Y-%m-%d")
            return date <= datetime.now()
        except ValueError:
            return False


    def is_valid_boolean(value):
        """
        Validate boolean inputs (e.g., 1 for True, 0 for False).
        :param value: The value to validate.
        :return: True if valid, False otherwise.
        """
        return str(value) in {"1", "0"}
