# ----------------------------------------
# Day 10 - Student Report
# Author: Shital Tukaram Ambekar
# Bootcamp: Python for Data Analyst
# ----------------------------------------

name = input("Enter student name: ")

python = int(input("Enter Python marks: "))
sql = int(input("Enter SQL marks: "))
excel = int(input("Enter Excel marks: "))

total = python + sql + excel
average = total / 3

print("\n========== Student Report ==========")
print("Student Name :", name)
print("Python Marks :", python)
print("SQL Marks    :", sql)
print("Excel Marks  :", excel)
print("Total Marks  :", total)
print("Average      :", round(average, 2))

if average >= 75:
    print("Grade        : Distinction")
elif average >= 60:
    print("Grade        : First Class")
elif average >= 35:
    print("Grade        : Pass")
else:
    print("Grade        : Fail")
