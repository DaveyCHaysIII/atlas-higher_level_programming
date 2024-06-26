#!/usr/bin/python3
"""write a script that lists all cities from hbtn_0e_4_usa"""

import sys
import MySQLdb


def list_states(username, password, database):

    db = MySQLdb.connect(
         host="localhost",
         user=username,
         passwd=password,
         db=database,
         port=3306
         )

    cursor = db.cursor()

    cursor.execute(
         "SELECT cities.id, cities.name, states.name "
         + "FROM states INNER JOIN cities "
         + "ON cities.state_id = states.id "
         + "ORDER BY cities.id"
         )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py " +
              "<mysql username> <mysql password> <database name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
