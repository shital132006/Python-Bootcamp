# Day 25 - List Traversing

## 📚 Topics Covered

- Traversing a List using `for` loop
- Accessing each element of a list
- append() Method
- insert() Method

---

## 📝 Definition

**List Traversing** means visiting each element of a list one by one using a loop.

---

## 💻 Programs

### Program 1 - Traversing a List

```python
cities = ["Mumbai", "Pune", "Delhi"]

for city in cities:
    print(city)
```

### Output

```
Mumbai
Pune
Delhi
```

---

### Program 2 - append()

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

### Output

```
[10, 20, 30, 40]
```

---

### Program 3 - insert()

```python
numbers = [10, 20, 40]

numbers.insert(2, 30)

print(numbers)
```

### Output

```
[10, 20, 30, 40]
```

---

## 🎯 What I Learned

- A `for` loop is used to access every element in a list.
- `append()` adds one item at the end of the list.
- `insert()` adds an item at a specific index.
- List traversal is very useful for processing datasets in Data Analysis.
