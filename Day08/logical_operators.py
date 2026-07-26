# ----------------------------------------
# Day 08 - Logical Operators
# Author: Shital Tukaram Ambekar
# Bootcamp: Python for Data Analyst
# ----------------------------------------

age = int(input("Enter your age: "))
citizen = input("Are you an Indian citizen? (yes/no): ").lower()

if age >= 18 and citizen == "yes":
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")

print("\nLogical Operator Examples")

print(True and True)
print(True and False)
print(True or False)
print(False or False)
print(not True)
print(not False)
