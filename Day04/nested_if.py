# ----------------------------------------
# Day 04 - Nested If
# Author: Shital Tukaram Ambekar
# Description: Demonstrates nested if statement.
# ----------------------------------------

age = int(input("Enter your age: "))
has_id = input("Do you have an ID card? (yes/no): ").lower()

if age >= 18:
    if has_id == "yes":
        print("You are eligible to enter.")
    else:
        print("You need an ID card.")
else:
    print("You are not eligible to enter.")
