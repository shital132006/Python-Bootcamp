# ----------------------------------------
# Day 11 - Employee Report
# Author: Shital Tukaram Ambekar
# Bootcamp: Python for Data Analyst
# ----------------------------------------

employee_name = input("Enter Employee Name: ")
salary = float(input("Enter Salary: "))
experience = int(input("Enter Years of Experience: "))

if experience >= 5:
    bonus = salary * 0.20
elif experience >= 2:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

total_salary = salary + bonus

print("\n========== Employee Report ==========")
print("Employee Name :", employee_name)
print("Salary        :", salary)
print("Experience    :", experience, "Years")
print("Bonus         :", bonus)
print("Total Salary  :", total_salary)
