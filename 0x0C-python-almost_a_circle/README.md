# 0x0C. Python - Almost a circle
# Background Context
In this project, I will review everything about Python:
* Import
* Exceptions
* Class
* Private attribute
* Getter/Setter
* Class method
* Static method
* Inheritance
* Unittest
* Read/Write file
I will also learn about:
* args and kwargs
* Serialization/Deserialization
* JSON
# Learning Objectives
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function
# Requirements
## Python Scripts
* Used editors: emacs
* All files were interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All files end with a new line
* The first line of all the files is #!/usr/bin/python3
* Code use the PEP 8 style (version 1.7.*)
* All files are executable
* The length of files were tested using wc
* All modules are documented: python3 -c 'print(__import__("my_module").__doc__)'
* All classes are documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
* All functions (inside and outside a class) are documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
## Python Unit Tests
* Used editors: emacs
* All files end with a new line
* All test files are inside a folder tests
* I used the unittest module
* All test files should be python files (extension: .py)
* All test files and folders start with test_
* File organization in the tests folder is the same as my project: ex: for models/base.py, unit tests must be in: tests/test_models/test_base.py
* All my tests should were by using this command: python3 -m unittest discover tests
* I can also test file by file by using this command: python3 -m unittest tests/test_models/test_base.py