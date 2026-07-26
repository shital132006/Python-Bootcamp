# ----------------------------------------
# Day 21 - Default & Step Slicing
# Author: Shital Tukaram Ambekar
# Bootcamp: Python for Data Analyst
# ----------------------------------------

word = "Amazon"

print("Original String :", word)

# Default Slicing
print("First Three Letters :", word[:3])
print("Last Three Letters  :", word[3:])
print("Complete String     :", word[:])

print()

text = "DataAnalyst"

# Step Slicing
print("Every Second Character :", text[::2])
print("Characters from Index 1:", text[1::2])
print("Step of 3              :", text[2:10:3])
