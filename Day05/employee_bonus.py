# ----------------------------------------
# Day 05 - Employee Bonus
# Author: Shital Tukaram Ambekar
# Description: Calculates bonus based on performance.
# ----------------------------------------

salary = float(input("Enter salary: "))
performance = input("Enter performance level (good/excellent): ").lower()

if performance == "excellent":
    bonus = salary * 0.20
elif performance == "good":
    bonus = salary * 0.10
else:
    bonus = 0

total_salary = salary + bonus

print("\n----- Employee Report -----")
print("Salary       :", salary)
print("Bonus        :", bonus)
print("Total Salary  :", total_salary)
