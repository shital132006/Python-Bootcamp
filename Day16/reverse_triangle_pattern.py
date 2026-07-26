# ----------------------------------------
# Day 16 - Reverse Triangle Pattern
# Author: Shital Tukaram Ambekar
# Bootcamp: Python for Data Analyst
# ----------------------------------------

for row in range(5):
    for col in range(5 - row):
        print("*", end="")
    print()
