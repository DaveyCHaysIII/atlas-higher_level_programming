#!/usr/bin/python3
"""write a script that lists state given from hbtn_0e_0_usa"""

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

    query = "SELECT * FROM 'states' WHERE 'name' = %s ORDER BY 'id'"
    cursor.execute(query, (statename,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./script.py"
              + " <mysql username> <mysql password> <database name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    statename = sys.argv[4]

    list_states(username, password, database, statename)
