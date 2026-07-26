# ----------------------------------------
# Day 04 - Student Report
# Author: Shital Tukaram Ambekar
# Description: Calculates total, average and result.
# ----------------------------------------

name = input("Enter student name: ")

sub1 = int(input("Enter marks in Subject 1: "))
sub2 = int(input("Enter marks in Subject 2: "))
sub3 = int(input("Enter marks in Subject 3: "))

total = sub1 + sub2 + sub3
average = total / 3

print("\n----- Student Report -----")
print("Name    :", name)
print("Total   :", total)
print("Average :", average)

if average >= 35:
    if average >= 75:
        print("Result  : Distinction")
    elif average >= 60:
        print("Result  : First Class")
    else:
        print("Result  : Pass")
else:
    print("Result  : Fail")
