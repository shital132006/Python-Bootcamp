# ----------------------------------------
# Day 22 - Reverse Slicing & Palindrome
# Author: Shital Tukaram Ambekar
# Bootcamp: Python for Data Analyst
# ----------------------------------------

word = input("Enter a word: ")

print("Original Word :", word)
print("Reversed Word :", word[::-1])

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
