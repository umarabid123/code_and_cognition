# 📁 Topic: Object-Oriented Programming (OOP) in Python

---

## 🎯 Learning Objectives

By the end of this session, you will be able to:

- Understand the concepts of **classes** and **objects** in Python
- Define and use **attributes** and **methods**
- Apply the four OOP principles: **Encapsulation**, **Abstraction**, **Inheritance**, **Polymorphism**
- Use **constructors** (`__init__` method) for object initialization
- Implement **real-world problem modeling** using OOP
- Work with **multiple objects** from a single class
- Understand **advantages** and **real-world applications** of OOP

---

## 📚 What is OOP?

- **Object-Oriented Programming (OOP)** is a programming approach that organizes code into **objects**.
- An **object** combines **data** (attributes) and **behavior** (methods).
- A **class** is a **blueprint** for creating objects.
- An **object** is an **instance** of a class.

💡 **Analogy:**
- **Class:** Car Blueprint  
- **Object:** Your Tesla Model S or Toyota Corolla

---

## 🏗️ OOP Terminology

| Term          | Description |
|---------------|-------------|
| **Class**     | Blueprint/template for creating objects |
| **Object**    | Instance of a class |
| **Attribute** | Variable inside a class that stores data |
| **Method**    | Function inside a class that defines behavior |
| **self**      | Refers to the current instance of the class |
| **Constructor** | Special method `__init__` used to initialize attributes |

---

## 📖 Creating a Class & Object

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving.")

# Creating objects
car1 = Car("Tesla", "Model S")
car2 = Car("Toyota", "Corolla")

car1.drive()  # Tesla Model S is driving.
car2.drive()  # Toyota Corolla is driving.


# Example 1: Car Class (Existing Example)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving.")

# Creating objects
car1 = Car("Tesla", "Model S")
car2 = Car("Toyota", "Corolla")

car1.drive()  # Tesla Model S is driving.
car2.drive()  # Toyota Corolla is driving.


# Example 2: Student Class
class Student:
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Grade: {self.grade}")

student1 = Student("Alice", 101, "A")
student2 = Student("Bob", 102, "B+")

student1.display_info()
student2.display_info()


# Example 3: BankAccount Class
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient funds!")

account1 = BankAccount("Charlie", 1000)
account1.deposit(500)
account1.withdraw(300)


# Example 4: Book Class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def book_info(self):
        print(f"'{self.title}' by {self.author} - ${self.price}")

book1 = Book("1984", "George Orwell", 15.99)
book2 = Book("The Alchemist", "Paulo Coelho", 12.50)

book1.book_info()
book2.book_info()



📘 Classes and Objects in Python
🎯 Learning Objectives
By the end of this session, you will be able to:

Understand what classes and objects are

Differentiate between blueprint (class) and instance (object)

Relate OOP to real-world examples

Identify use cases for classes and objects

1️⃣ What is a Class?
A class is a blueprint or template for creating objects.

It defines:

Attributes → data or properties

Methods → actions or behaviors

💡 Analogy:
Class = "House blueprint"
It describes how the house will look, but it’s not an actual house yet.

2️⃣ What is an Object?
An object is an instance of a class.

Every object created from a class has:

Its own attribute values

Access to the same methods defined in the class

💡 Analogy:
Object = "A real house built from the blueprint"
You can have many houses from the same blueprint, but each may have different paint colors, furniture, etc.

3️⃣ How They Work Together
Define a class → acts like a recipe

Create objects → actual dishes made using that recipe

4️⃣ Python Example
python
Copy
Edit
# Defining a class
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

    def drive(self):  # Method
        print(f"{self.brand} {self.model} is driving.")

# Creating objects (instances)
car1 = Car("Tesla", "Model S")
car2 = Car("Toyota", "Corolla")

# Using objects
car1.drive()  # Output: Tesla Model S is driving.
car2.drive()  # Output: Toyota Corolla is driving.