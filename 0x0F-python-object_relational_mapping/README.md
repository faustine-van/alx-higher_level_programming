# python object relational mapping
In this project, I link two amazing worlds: Databases and Python!

In the first part, I used the module MySQLdb to connect to a MySQL database
and execute your SQL queries.

In the second part, I used the module SQLAlchemy an Object Relational Mapper (ORM).

## Resources

[Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
[mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/)
[MySQLdb tutorial](https://www.mikusa.com/python-mysql-docs/index.html)
[SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
[SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
[mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)
[Introduction to SQLAlchemy]()
[Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
[10 common stumbling blocks for SQLAlchemy newbies](http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
[Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
[SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
[SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)
[Python Virtual Environments: A primer](https://realpython.com/python-virtual-environments-a-primer/)
[More about mysql](https://mysql-python.sourceforge.net/MySQLdb.html#some-examples)
[Mysql injection](https://stackoverflow.com/questions/7929364/python-best-practice-and-securest-way-to-connect-to-mysql-and-execute-queries)
[Sql injection](https://en.wikipedia.org/wiki/SQL_injection)
[Interacting with a Database using SQLAlchemy: CRUD Operations](https://vegibit.com/interacting-with-a-database-using-sqlalchemy-crud-operations/)
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
