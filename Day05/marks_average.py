# ----------------------------------------
# Day 05 - Marks Average
# Author: Shital Tukaram Ambekar
# Description: Calculates total and average marks.
# ----------------------------------------

name = input("Enter student name: ")

m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))
m4 = int(input("Enter marks 4: "))
m5 = int(input("Enter marks 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

print("\n----- Result -----")
print("Name    :", name)
print("Total   :", total)
print("Average :", average)

if average >= 35:
    print("Status  : Pass")
else:
    print("Status  : Fail")
