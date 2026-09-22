class Employee:

    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid Amount")

    @salary.deleter
    def salary(self):
        del self.__salary

    def display_details(self):
        print(f"Employee ID   : {self.emp_id}")
        print(f"Employee Name : {self.emp_name}")
        print(f"Salary        : {self.salary}")


class Developer(Employee):

    def __init__(self, emp_id, emp_name, salary, programming_lang):
        super().__init__(emp_id, emp_name, salary)
        self.programming_lang = programming_lang

    def display_details(self):
        super().display_details()
        print(f"Role                : Developer")
        print(f"Programming Language : {self.programming_lang}")

    def write_code(self):
        print(
            f"{self.emp_name} is developing application "
            f"using {self.programming_lang}"
        )


class Manager(Employee):

    def __init__(self, emp_id, emp_name, salary, team_size):
        super().__init__(emp_id, emp_name, salary)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print(f"Role      : Manager")
        print(f"Team Size : {self.team_size}")

    def manage_team(self):
        print(
            f"{self.emp_name} is managing team "
            f"of size {self.team_size}"
        )