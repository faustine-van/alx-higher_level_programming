#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N) from the database
script that lists all states from the database hbtn_0e_0_usa
script should take 3 arguments: mysql username,mysql password and database name
use the module MySQLdb (import MySQLdb)
script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id

"""
import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    connection = MySQLdb.connect(
        host="localhost", port=3306, user=args[1], passwd=args[2],
        db=args[3], charset="utf8")
    cur = connection.cursor()
    cur.execute("SELECT * FROM states WHERE name REGEXP '^N' ORDER BY id ASC")
    queryRows = cur.fetchall()
    for row in queryRows:
        print(row)
    cur.close()
    connection.close()
