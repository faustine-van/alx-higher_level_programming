#!/usr/bin/python3
"""
- script that lists all cities from the database hbtn_0e_4_usa
script should take 3 arguments: mysql username,mysql password and database name
use the module MySQLdb (import MySQLdb)
script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id

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
    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN\
        states ON cities.state_id = states.id ORDER BY states.id ASC"
    cur.execute(query)

    # Fetch all the rows and display the results
    queryRows = cur.fetchall()
    for row in queryRows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    connection.close()
