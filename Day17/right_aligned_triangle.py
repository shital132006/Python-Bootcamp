# ----------------------------------------
# Day 17 - Right Aligned Triangle Pattern
# Author: Shital Tukaram Ambekar
# Bootcamp: Python for Data Analyst
# ----------------------------------------

for row in range(5):
    for col in range(5 - row - 1):
        print(" ", end="")
    for col in range(row + 1):
        print("*", end="")
    print()
