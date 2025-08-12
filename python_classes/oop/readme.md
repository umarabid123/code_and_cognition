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
