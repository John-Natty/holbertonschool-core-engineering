# Python - Inheritance & Polymorphism

## Description

In many programs, different objects represent variations of the same concept. For example, different geometric shapes may share common characteristics, and different types of users may share similar behavior.

Object-oriented programming allows us to represent these relationships using inheritance.

Inheritance allows a class to reuse and extend behavior from another class. A class that inherits from another class automatically receives its attributes and methods, and it can also modify or extend them.

Another closely related concept is polymorphism. Polymorphism allows different objects to respond to the same method call in different ways depending on their class.

Together, inheritance and polymorphism allow developers to design systems that are easier to maintain, extend, and understand.

In this project, you will explore these concepts by building a hierarchy of geometric shapes.

## Learning Objectives

By completing this project, you should be able to:

- Explain how inheritance allows classes to reuse behavior
- Identify parent classes and child classes
- Create subclasses that extend the behavior of another class
- Override inherited methods
- Understand how polymorphism allows objects of different classes to respond to the same method call
- Use isinstance() to check object relationships
- Use issubclass() to check class relationships
- Design simple inheritance hierarchies

## Class Hierarchy in This Project

Throughout this project you will progressively build the following class hierarchy:
```
BaseGeometry
     |
     ▼
 Rectangle
     |
     ▼
   Square
```

Interpretation 

- BaseGeometry defines behavior shared by geometric shapes.
- Rectangle inherits from BaseGeometry and implements concrete behavior.
- Square inherits from Rectangle and represents a more specialized shape.

Because Square inherits from Rectangle, and Rectangle inherits from BaseGeometry, a Square object can also be treated as:

- a Rectangle
- a BaseGeometry

This relationship enables code reuse and polymorphism, allowing programs to work with related objects through a shared interface.

## Requirements

- Operating system: Ubuntu 20.04 LTS
- Python version: Python 3.8.x
- Code style: `pycodestyle` 2.7.x
- All Python files must start with:

```python
#!/usr/bin/env python3
```

## Coding rules

- All files must end with a newline
- Code must follow PEP8
- All modules, classes, and functions must include documentation strings
- Only the Python standard library may be used unless otherwise stated
- Do not use the words import or from inside your comments, the checker will think you are trying to import some modules.
- To import any base class use the __import__method.