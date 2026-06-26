'''
Docstring for Assignment09.a16
Smart Loan Eligibility System

A bank approves loans based on salary, age, credit score, and EMI.

If salary is 40000 or above, then check age. If age is between 21 and 60, then check credit score. If credit score is 750 or above, then check EMI. If EMI is less than or equal to 40% of salary, approve at 8%; otherwise approve at 10%. If credit score is below 750, then check if it is at least 650. If yes, approve at 12%; otherwise reject.

If salary is below 40000, then check if salary is at least 25000 and credit score is at least 700. If yes, approve at 13%; otherwise reject.

Input:
Salary = 50000
Age = 30
Credit Score = 760
EMI = 18000

Output:
Loan Status = Approved at 8%
'''
salary = int(input("Enter Salary: "))
age = int(input("Enter Age: "))
credit_score = int(input("Enter Credit Score: "))
emi = int(input("Enter Monthly EMI: "))