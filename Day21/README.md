# Day 21 - Default & Step Slicing

## Topics Covered

- Default Slicing
- Step Slicing
- Omitting Start Index
- Omitting End Index

## Examples

word = "Amazon"

word[:3]   → Ama

word[3:]   → zon

word[:]    → Amazon

text = "DataAnalyst"

text[::2]
text[1::2]
text[2:10:3]

## What I Learned

- If the starting index is omitted, Python starts from index 0.
- If the ending index is omitted, Python goes to the end of the string.
- Step slicing skips characters according to the given step value.
- Step slicing is useful for extracting patterns from text.
