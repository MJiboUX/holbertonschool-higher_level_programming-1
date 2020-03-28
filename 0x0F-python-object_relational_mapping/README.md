# 0x0F. Python - Object-relational mapping
# Learning Objectives
* Why Python programming is awesome
* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table
# Requirements
* Allowed editors: ```vi```, ```vim```, ```emacs```
* All files were interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* My files were executed with ```MySQLdb``` version ```1.3.x```
* My files were executed with ```SQLAlchemy``` version ```1.2.x```
* All files end with a new line
* The first line of all files should is ```#!/usr/bin/python3```
* My code use the ```PEP 8``` style (```version 1.7.*```)
* All files are executable
* The length of files were tested using ```wc```
* All modules have a documentation (```python3 -c 'print(__import__("my_module").__doc__)'```)
* All classes have a documentation (```python3 -c 'print(__import__("my_module").MyClass.__doc__)'```)
* All functions (inside and outside a class) should have a documentation (```python3 -c 'print(__import__("my_module").my_function.__doc__)'``` and ```python3 -c print(__import__("my_module").MyClass.my_function.__doc__)'```)
* I'm not allowed to use execute with sqlalchemy
# More Info
## Install MySQLdb module version 1.3.x
For installing ```MySQLdb```, you need to have ```MySQL``` installed:
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==1.3.10
...
$ python3
>>> import MySQLdb
>>> MySQLdb.__version__
'1.3.10'
```
## Install ```SQLAlchemy``` module version ```1.2.x```
```
$ pip3 install SQLAlchemy==1.2.5
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.2.5'
```
Also, you can have this warming message:
```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
    ```

    You can ignore it.
```