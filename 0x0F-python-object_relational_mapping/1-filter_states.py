#!/usr/bin/python3
"""A script that lists all states with a name starting with N (upper N)
   from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    command = "SELECT * FROM states WHERE states.name LIKE 'N%' ORDER BY st\
ates.id"
    cur.execute(command)
    rows = cur.fetchall()
    for row in rows:
        print("({}, '{}')".format(row[0], row[1]))
    cur.close()
