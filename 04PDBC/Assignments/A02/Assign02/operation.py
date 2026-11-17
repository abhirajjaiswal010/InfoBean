from db import get_connection
from tabulate import tabulate


def addDepartment():

    try:
        con = get_connection()
        cur = con.cursor()

        id = int(input("Enter Id :"))
        name = input("Enter department Name : ")
        location = input("Enter Location : ")

        query = """
    insert into department_pdbc
    values(%s,%s,%s)
    """
        values = (id, name, location)

        cur.execute(query, values)

        if cur.rowcount > 0:
            print("Add Department SuccessFully")
        else:
            print("Add Department Failed")
    except Exception as e:
        print("Something went wrong!")
        print("Error:", e)

    finally:
        cur.close()
        con.close()


def addEmployee():
    con = get_connection()
    cur = con.cursor()

    try:
        id = int(input("Enter Id: "))
        name = input("Enter Name: ")
        salary = int(input("Enter Salary: "))
        title = input("Enter Title: ")
        did = int(input("Enter Dept Id: "))
        manager_id = int(input("Enter Manager Id (or empty for no manager):"))
        if manager_id == "":
            manager_id = None
        else:
            manager_id = int(manager_id)

        query = """
        INSERT INTO employee_pdbc
        VALUES (%s,%s,%s,%s,%s,%s)
        """

        values = (id, name, salary, title, did, manager_id)

        cur.execute(query, values)
        con.commit()

        if cur.rowcount > 0:
            print("Employee Added Successfully")
        else:
            print("Employee Addition Failed")

    except Exception as e:
        con.rollback()
        print("Error:", e)

    finally:
        cur.close()
        con.close()


def displayAll():
    con = get_connection()
    cur = con.cursor()

    try:

        query = """
         select e.emp_id,e.emp_name,e.job_title,e.salary,d.dept_name
    from employee_pdbc e
    join department_pdbc d
    on e.dept_id=d.dept_id;
        """

        cur.execute(query)
        result = cur.fetchall()
        header = ["emp_id", "emp_name", "job_title", "salary", "department"]

        print(tabulate(result, headers=header, tablefmt="rounded_grid"))

    except Exception as e:

        print("Error:", e)

    finally:
        cur.close()
        con.close()


def searchEmp():
    con = get_connection()
    cur = con.cursor()

    try:

        name = input("/nEnter Name :  ")

        query = """
         select emp_id,emp_name,job_title,salary
         from employee_pdbc
         where emp_name like %s;
        """

        cur.execute(query, ("%" + name + "%",))
        result = cur.fetchall()
        header = ["emp_id", "emp_name", "job_title", "salary"]

        print(tabulate(result, headers=header, tablefmt="rounded_grid"))

    except Exception as e:

        print("Error:", e)

    finally:
        cur.close()
        con.close()


def updateEmployeeSalary():
    con = get_connection()
    cur = con.cursor()

    try:
        id = int(input("/nEnter Id : "))
        salary = int(input("/nEnter New Salary :"))

        query = """
         update employee_pdbc
         set salary=%s
         where emp_id=%s
        """

        cur.execute(query, (salary, id))

        if cur.rowcount > 0:
            print("Salary Update Successed")
        else:
            print("Salary Update Failed")

    except Exception as e:

        print("Error:", e)

    finally:
        cur.close()
        con.close()

def updateEmployeeDept():
    con = get_connection()
    cur = con.cursor()

    try:
        id = int(input("/nEnter Id : "))
        did = int(input("/nEnter New Dept Id :"))

        query = """
         update employee_pdbc
         set dept_id=%s
         where emp_id=%s
        """

        cur.execute(query, (did, id))

        if cur.rowcount > 0:
            print("Department Update Successed")
        else:
            print("Department Update Failed")

    except Exception as e:

        print("Error:", e)

    finally:
        cur.close()
        con.close()

def deleteEmployee():
    con = get_connection()
    cur = con.cursor()

    try:
        id = int(input("/nEnter Id : "))
        
        query = """
         delete from employee_pdbc
         where emp_id=%s
        """

        cur.execute(query, (id,))

        if cur.rowcount > 0:
            print("Delete Successed")
        else:
            print("Delete  Failed")

    except Exception as e:

        print("Error:", e)

    finally:
        cur.close()
        con.close()
    
def displayDeptEmpCount():
    con = get_connection()
    cur = con.cursor()

    try:

        

        query = """
         SELECT d.dept_name, COUNT(e.emp_id) AS Emp_count
FROM department_pdbc d, employee_pdbc e
WHERE d.dept_id = e.dept_id
GROUP BY d.dept_name;;
        """

        cur.execute(query)
        result = cur.fetchall()
        header = ["department_name", "Empployee_count"]

        print(tabulate(result, headers=header, tablefmt="rounded_grid"))

    except Exception as e:

        print("Error:", e)

    finally:
        cur.close()
        con.close()

def displayDeptAvgSalary():
    con = get_connection()
    cur = con.cursor()

    try:

        

        query = """
         SELECT d.dept_name, avg(e.salary) AS emp_avg
FROM department_pdbc d, employee_pdbc e
WHERE d.dept_id = e.dept_id
GROUP BY d.dept_name
        """

        cur.execute(query)
        result = cur.fetchall()
        header = ["department_name", "Average_salary"]

        print(tabulate(result, headers=header, tablefmt="rounded_grid"))

    except Exception as e:

        print("Error:", e)

    finally:
        cur.close()
        con.close()
    
def EmpEarningMoreAvgSalary():
    con = get_connection()
    cur = con.cursor()

    try:

        

        query = """
         SELECT emp_id, emp_name,salary
FROM employee_pdbc
WHERE salary>(
select avg(salary)
from employee_pdbc)
        """

        cur.execute(query)
        result = cur.fetchall()
        header = ["emp_id", "emp_name","salary"]

        print(tabulate(result, headers=header, tablefmt="rounded_grid"))

    except Exception as e:

        print("Error:", e)

    finally:
        cur.close()
        con.close()

def empEarnMoredeptAvg():
    con = get_connection()
    cur = con.cursor()

    try:

        

        query = """
         SELECT 
    e1.emp_id,
    e1.emp_name,
    d1.dept_name,
    e1.salary
FROM employee_pdbc e1, department_pdbc d1
WHERE e1.dept_id = d1.dept_id
AND e1.salary > (
    SELECT AVG(e2.salary)
    FROM employee_pdbc e2
    WHERE e1.dept_id = e2.dept_id
);
        """

        cur.execute(query)
        result = cur.fetchall()
        header = ["emp_id", "emp_name","department","salary"]

        print(tabulate(result, headers=header, tablefmt="rounded_grid"))

    except Exception as e:

        print("Error:", e)

    finally:
        cur.close()
        con.close()



def displayEmpWorkAtIt():
    con = get_connection()
    cur = con.cursor()

    try:

        

        query = """
         SELECT 
    e1.emp_id,
    e1.emp_name,
    e1.salary
FROM employee_pdbc e1,department_pdbc d
WHERE d.dept_name="it" and d.dept_id=e1.dept_id;
        """

        cur.execute(query)
        result = cur.fetchall()
        header = ["emp_id", "emp_name","salary"]

        print(tabulate(result, headers=header, tablefmt="rounded_grid"))

    except Exception as e:

        print("Error:", e)

    finally:
        cur.close()
        con.close()

def displayDeptMoreOneEmp():
    con = get_connection()
    cur = con.cursor()

    try:

        

        query = """
         select d.dept_name,count(e.emp_id) from department_pdbc d ,employee_pdbc e where d.dept_id=e.dept_id  group by d.dept_id having count(e.emp_id)>1
        """

        cur.execute(query)
        result = cur.fetchall()
        header = ["department_name", "employee_count "]

        print(tabulate(result, headers=header, tablefmt="rounded_grid"))

    except Exception as e:

        print("Error:", e)

    finally:
        cur.close()
        con.close()

def displayEmpManager():
    con = get_connection()
    cur = con.cursor()

    try:

        

        query = """
        SELECT e1.emp_name, m1.emp_name
        FROM employee_pdbc e1
        JOIN employee_pdbc m1
        ON e1.manager_id = m1.emp_id;
        """

        cur.execute(query)
        result = cur.fetchall()
        header = ["employee_name", "manager_name"]

        print(tabulate(result, headers=header, tablefmt="rounded_grid"))

    except Exception as e:

        print("Error:", e)

    finally:
        cur.close()
        con.close()

def displayDeptWithNoEmp():
    con = get_connection()
    cur = con.cursor()

    try:

        

        query = """
        SELECT d.dept_id, d.dept_name
FROM department_pdbc d
LEFT JOIN employee_pdbc e
ON d.dept_id = e.dept_id
WHERE e.dept_id IS NULL
        """

        cur.execute(query)
        result = cur.fetchall()
        header = ["Departmet_id", "department_name"]

        print(tabulate(result, headers=header, tablefmt="rounded_grid"))

    except Exception as e:

        print("Error:", e)

    finally:
        cur.close()
        con.close()


def checkForeignKeyConstraint():
    con = get_connection()
    cur = con.cursor()

    try:
        id = int(input("Enter Id: "))
        name = input("Enter Name: ")
        salary = int(input("Enter Salary: "))
        title = input("Enter Title: ")
        did = int(input("Enter Dept Id: "))
        manager_id = int(input("Enter Manager Id (or empty for no manager):"))
        if manager_id == "":
            manager_id = None
        else:
            manager_id = int(manager_id)

        query = """
        INSERT INTO employee_pdbc
        VALUES (%s,%s,%s,%s,%s,%s)
        """

        values = (id, name, salary, title, did, manager_id)

        cur.execute(query, values)
        con.commit()

        if cur.rowcount > 0:
            print("Employee Added Successfully")
        else:
            print("Employee Addition Failed")

    except Exception as e:
        con.rollback()
        print("Error:", e)

    finally:
        cur.close()
        con.close()
