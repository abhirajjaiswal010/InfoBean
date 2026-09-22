from model.employee import Employee, Developer, Manager
from rich.prompt import Prompt


emp_id = input("Enter Employee Id     : ")
emp_name = input("Enter Employee Name :")
salary = int(input("Enter Salary : "))
role=''

choice = Prompt.ask(
    "Choose Role",
    choices=["Developer", "Manager"]
)


if role=="Developer":
    programming_lang=input("Enter Programming Language  :")
    d1=Developer(emp_id,emp_name,salary,programming_lang)
    d1.display_details()
    d1.write_code()

else:
    team_size=int(input("Enter Team Size : "))
    m1=Manager(emp_id,emp_name,salary,team_size)
    m1.display_details()
    m1.manage_team()
