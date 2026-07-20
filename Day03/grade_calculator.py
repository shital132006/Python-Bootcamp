# ----------------------------------------
# Day 03 - Grade Calculator
# Author: Shital Tukaram Ambekar
# Description: Calculate grade using marks.
# ----------------------------------------

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")
