#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    try:
        args = sys.argv
        connection = MySQLdb.connect(
            host="localhost", port=3306, user=args[1], passwd=args[2],
            db=args[3], charset="utf8")
        cur = connection.cursor()
        cur.execute('SELECT * FROM states WHERE name = %s', (args[4],))
        queryRows = cur.fetchall()
        for row in queryRows:
            print(row)
    except MySQLdb.Error as e:
        print(e)
    finally:
        cur.close()
        connection.close()
