#!/usr/bin/python3
"""write a script that lists all cities from hbtn_0e_4_usa"""

import sys
import MySQLdb


def list_states(username, password, database, statename):

    db = MySQLdb.connect(
         host="localhost",
         user=username,
         passwd=password,
         db=database,
         port=3306
         )

    cursor = db.cursor()

    query = ("SELECT cities.name "
             + "FROM states INNER JOIN cities "
             + "ON cities.state_id = states.id "
             + "WHERE states.name = %s"
             + "ORDER BY cities.id")

    cursor.execute(query, (statename,))

    rows = cursor.fetchall()

    first = True
    for row in rows:
        if first:
            print(row, end="")
            first = False
        else:
            print(', ' + row[0], end="")
        print()

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./script.py " +
              "<mysql username> <mysql password> <database name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    statename = sys.argv[4]

    list_states(username, password, database, statename)
