# ----------------------------------------
# Day 07 - if, elif, else
# Author: Shital Tukaram Ambekar
# Bootcamp: Python for Data Analyst
# ----------------------------------------

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 35:
    print("Grade C")
else:
    print("Fail")
