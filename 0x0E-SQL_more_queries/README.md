# 0x0E. SQL - More queries
# Learning Objectives
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* Whats a PRIMARY KEY
* Whats a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION
# Requirements
* Allowed editors: vi, vim, emacs
* All files were executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
* All files end with a new line
* All SQL queries have a comment just before (i.e. syntax above)
* All files start by a comment describing the task
* All SQL keywords are in uppercase (SELECT, WHERE)
* The length of files were tested using wc
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
If you had before MySQL 5.5 installed, please run these 2 commands after the installation of the version 5.7:
```
$ mysql_upgrade -u root -p
Password:
$ sudo service mysql restart
```
If you have some issues to upgrade to 5.7, dont hesitate to cleanup your server of any MySQL packages: sudo apt-get remove --purge mysql-server mysql-client mysql-common
# How to import a SQL dump
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password:
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password:
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password:
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```