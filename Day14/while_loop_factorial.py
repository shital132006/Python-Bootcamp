# ----------------------------------------
# Day 14 - While Loop Factorial
# Author: Shital Tukaram Ambekar
# Bootcamp: Python for Data Analyst
# ----------------------------------------

num = int(input("Enter a number: "))

factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print("Factorial =", factorial)
