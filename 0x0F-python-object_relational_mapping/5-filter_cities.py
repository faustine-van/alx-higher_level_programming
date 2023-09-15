#!/usr/bin/python3
"""
- script that takes in the name of a state as an argument and lists all cities
  of that state, using the database hbtn_0e_4_usa(SQL injection free)
script should take 3 arguments: mysql username,mysql password and database name
use the module MySQLdb (import MySQLdb)
script should connect to a MySQL server running on localhost at port 3306

"""
import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv

    # Connect to the MySQL server
    connection = MySQLdb.connect(
        host="localhost", port=3306, user=args[1], passwd=args[2],
        db=args[3], charset="utf8")

    # Create a cursor object
    cur = connection.cursor()

    # Execute the SQL query to select states with names starting with 'N'
    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id =\
        states.id WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(query, (args[4],))

    # Fetch all the rows and display the results
    queryRows = cur.fetchall()

    # print(queryRows[-1])
    for i, row in enumerate(queryRows):
        # print(row[0], end=", " if row != queryRows[-1] else "\n")
        print(row[0], end=", " if i < len(queryRows) - 1 else "\n")

    # Close the cursor and the database connection
    cur.close()
    connection.close()
