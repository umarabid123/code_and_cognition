# Topic 1: Understanding Dictionaries in Python
## Learning Objectives
- By the end of this session, you will be able to:
- Understand what a dictionary is and why it's important
- Create, access, modify, and delete dictionary data
- Use built-in dictionary methods effectively

###  Introduction: What is a Dictionary in Python?
- A dictionary is a built-in Python data structure used to store data in key-value pairs.
It is: 
-  Mutable
-  Unordered (prior to Python 3.6)
-  Indexed by keys (not positions)

**Syntax:**
```
person = {"name": "Hanzla", "age": 22, "city": "Faisalabad"}
```

### 🧱 Core Concepts and Syntax

| Concept           | Example                                 |
|-------------------|------------------------------------------|
| Empty Dictionary  | `my_dict = {}` or `dict()`              |
| Adding Item       | `my_dict["key"] = value`                |
| Accessing Value   | `my_dict["key"]` or `my_dict.get("key")`|
| Updating Value    | `my_dict["key"] = new_value`            |
| Deleting Item     | `del my_dict["key"]` or `my_dict.pop("key")` |


####  Accessing and Modifying Dictionary Data
```
person["name"]        # Direct access
person.get("name")    # Safer access (returns None if key not found)
person["age"] = 23    # Update
person["country"] = "Pakistan"  # Add new key

```
#### 🔁 Looping Through Dictionaries
```
# Loop through keys
for key in person:
    print(key)

# Loop through values
for value in person.values():
    print(value)

# Loop through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```
#### ❌ Removing Items
```
person.pop("age")         # Removes a key and returns its value
del person["name"]        # Deletes key-value pair
person.clear()            # Removes all items

```
## 🧰 Essential Dictionary Methods

| Method              | Purpose                                 |
|---------------------|------------------------------------------|
| `get(key)`          | Returns value or `None`                  |
| `keys()`            | Returns all keys                         |
| `values()`          | Returns all values                       |
| `items()`           | Returns key-value pairs                  |
| `update(other_dict)`| Merges another dictionary                |
| `pop(key)`          | Removes and returns value of key         |
| `popitem()`         | Removes the last inserted item           |
| `clear()`           | Empties the dictionary                   |
| `copy()`            | Creates a shallow copy                   |


####  Nested Dictionaries
Useful for storing complex data structures (e.g., student records):

```
students = {
    "101": {"name": "Ali", "marks": 92},
    "102": {"name": "Sara", "marks": 88}
}
```
Access nested values:

```
students["101"]["name"]  # Output: Ali
```


#### 🛠️ Real-World Example: Word Frequency Counter
```
text = "python is fun and python is powerful"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)
```
💡 Best Practices
```
Use .get() to avoid KeyError
```
- Use meaningful and consistent key names

- Prefer defaultdict for automatic default values (via collections)

- Use update() to merge safely

- Avoid using mutable data types as keys

#### ✅ Quick Recap
Dictionaries are powerful, flexible, and easy to use

Allow fast data lookup via keys

Support a variety of built-in methods

Useful in many real-world applications: configuration files, caches, APIs, etc.

#### 🧩 Activity/Challenge
- Create a dictionary that tracks stock quantities and prices for 5 products.
Allow the user to input a product and return its price and quantity.