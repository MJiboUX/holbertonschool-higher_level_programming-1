#!/usr/bin/python3
"""
A script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. But this time it'ss safe
from MySQL injections!
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY %s
                   ORDER BY id;""", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print("({}, '{}')".format(row[0], row[1]))
    cur.close()
