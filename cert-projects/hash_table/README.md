# Hash Table

A custom hash table implementation built from scratch in Python, without
using Python's built-in dictionary hashing — demonstrates understanding
of how key-value lookups work under the hood.

## Features
- Custom hash function using character ordinal values
- Handles hash collisions by storing multiple key-value pairs under
  the same hash bucket
- Add, remove, and lookup operations

## Example
```python
table = HashTable()
table.add("name", "Aldrei")
print(table.lookup("name"))  # Aldrei
```

## What I'd add next
- A better hash function to reduce collision likelihood
- Automatic resizing as the table grows
