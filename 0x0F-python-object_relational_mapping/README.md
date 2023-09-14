# python object relational mapping
In this project, I link two amazing worlds: Databases and Python!

In the first part, I used the module MySQLdb to connect to a MySQL database
and execute your SQL queries.

In the second part, I used the module SQLAlchemy an Object Relational Mapper (ORM).

## Resources

[Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
[mysqlclient/MySQLdb documentation]()
[MySQLdb tutorial]()
[SQLAlchemy tutorial]()
[SQLAlchemy]()
[mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)
[Introduction to SQLAlchemy]()
[Flask SQLAlchemy]()
[10 common stumbling blocks for SQLAlchemy newbies]()
[Python SQLAlchemy Cheatsheet]()
[SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)]()
[SQLAlchemy Tutorial]()
[Python Virtual Environments: A primer](https://realpython.com/python-virtual-environments-a-primer/)

## More Info
### Install and activate venv

To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:
```
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

### Install MySQLdb module version 2.0.x
For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info
(2, 0, 3, 'final', 0)
```

### Install SQLAlchemy module version 1.4.x
$ sudo pip3 install SQLAlchemy
...
```
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.4.22'
```
Also, you can have this warning message:
```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")
  cursor.execute(statement, parameters)
```
You can ignore it.

## AUTHOR:
* [Fautsine]()
