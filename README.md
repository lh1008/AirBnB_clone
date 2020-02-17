# 0x00. AirBnB clone - The console

## Learning Objectives


- How to create a Python package
- How to create a command interpreter in Python using the `cmd` module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage `datetime`
- What is an `UUID`
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function


## Tasks

_**0. README, AUTHORS**_  
Write a README.md

_**1. Be PEP8 compliant!**_  
Write beautiful code that passes the PEP8 checks.

_**2. Unittests**_  
All your files, classes, functions must be tested with unit tests.

_**3. BaseModel**_  
Write a class `BaseModel` that defines all common attributes/methods for other classes.

_**4. Create BaseModel from dictionary**_  
Previously we created a method to generate a dictionary representation of an instance (method `to_dict()`).

_**5. Store first object**_  
Now we can recreate a `BaseModel` from another one by using a dictionary representation.

_**6. Console 0.0.1**_  
Write a program called `console.py` that contains the entry point of the command interpreter.

_**7. Console 0.1**_  
Update your command interpreter (`console.py`) to have these commands.

_**8. First User**_  
Write a class `User` that inherits from `BaseModel`.

_**9. More classes!**_  
Write all those classes that inherit from `BaseModel`.

_**10. Console 1.0**_  
Update `FileStorage` to manage correctly serialization and deserialization of all our new classes: `Place`, `State`, `City`, `Amenity` and `Review`.  

Update your command interpreter (`console.py`) to allow those actions: `show`, `create`, `destroy`, `update` and `all` with all classes created previously.

Enjoy your first console!
