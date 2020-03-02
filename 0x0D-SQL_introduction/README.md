# 0x0D. SQL - Introduction
# Learning Objectives
* Whats a database
* Whats a relational database
* What does SQL stand for
* Whats MySQL
* How to create a database in MySQL
* What does DDL and DML stand for
* How to CREATE or ALTER a table
* How to SELECT data from a table
* How to INSERT, UPDATE or DELETE data
* What are subqueries
* How to use MySQL functions
# Requirements
* Allowed editors: vi, vim, emacs
* All files were executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
* All files end with a new line
* All SQL queries have a comment just before (i.e. syntax above)
* All files start by a comment describing the task
* All SQL keywords are in uppercase (SELECT, WHERE)
* The length of files were tested using wc
# Shoutouts
* San Franciscos Anne Cognet
* San Franciscos John Coleman
# Comments for a SQL file:
```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
# Install MySQL 5.7 on Ubuntu 14.04 LTS
```
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
$
```
**Dont forget your root password**
Connect to your MySQL server:
```
$ mysql -hlocalhost -uroot -p
Password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 42
Server version: 5.7.8-rc MySQL Community Server (GPL)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
```
If you have some issues to upgrade to 5.7, dont hesitate to cleanup your server of any MySQL packages: sudo apt-get remove --purge mysql-server mysql-client mysql-common