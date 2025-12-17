#Loops in Python

This README provides a clear and practical overview of the main **looping structures in Python**, focusing on:

* `for` loops
* the `in` keyword
* the `range()` function
* nested loops

These concepts are **fundamental for Python developers**, especially in **data engineering, automation, and machine learning**.

---

## What are loops?

Loops allow you to **execute a block of code multiple times**, avoiding manual repetition and making your code more **clean, scalable, and readable**.

In Python, the most commonly used loop is the `for` loop.

---

## The `for` Loop

The `for` loop is used to **iterate over a sequence**, such as lists, strings, tuples, dictionaries, or any iterable object.

### Basic syntax:

```python
for item in iterable:
    # code block
```

### Example:

```python
numbers = [1, 2, 3, 4]

for number in numbers:
    print(number)
```

Output:

```
1
2
3
4
```

---

## The `in` Keyword

The `in` keyword is used to **check membership** and to define **what the loop iterates over**.

### Example with a list:

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
```

### Example with a string:

```python
for letter in "Python":
    print(letter)
```

---

## The `range()` Function

The `range()` function generates a sequence of numbers and is commonly used with `for` loops.

### Syntax:

```python
range(start, stop, step)
```

* `start` → starting value (default: `0`)
* `stop` → ending value (not included)
* `step` → increment value (default: `1`)

### Example:

```python
for i in range(5):
    print(i)
```

Output:

```
0
1
2
3
4
```

### Example with `start` and `step`:

```python
for i in range(1, 10, 2):
    print(i)
```

Output:

```
1
3
5
7
9
```

---

## Nested Loops

Nested loops are **loops inside other loops**. They are useful when working with **matrices, grids, combinations, or multi-dimensional data**.

### Example:

```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```

Output:

```
i=0, j=0
i=0, j=1
i=1, j=0
i=1, j=1
i=2, j=0
i=2, j=1
```

### How it works:

* The **outer loop** runs first
* For each iteration of the outer loop, the **inner loop runs completely**

---

## Performance Considerations

Be careful with nested loops, especially when working with large datasets, as they can **increase time complexity**.

Whenever possible:

* Use built-in Python functions
* Prefer vectorized operations
* Consider libraries like **NumPy**, **Pandas**, or **PySpark** for large-scale data processing

---

## Best Practices

* Use meaningful variable names
* Keep loops simple and readable
* Avoid unnecessary nesting
* Write Pythonic code when possible

---

## Summary

| Concept      | Description                      |
| ------------ | -------------------------------- |
| `for`        | Iterates over an iterable        |
| `in`         | Defines membership and iteration |
| `range()`    | Generates numeric sequences      |
| Nested loops | Loops inside loops               |

---

This README covers the core concepts needed to confidently work with loops in Python and serves as a solid foundation for more advanced programming topics.
