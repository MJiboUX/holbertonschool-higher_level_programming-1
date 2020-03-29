#!/usr/bin/python3
""" A script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                   FROM states, cities
                   WHERE cities.state_id = states.id
                   ORDER BY cities.id""")
    rows = cur.fetchall()
    for row in rows:
        print("({}, '{}', '{}')".format(row[0], row[1], row[2]))
    cur.close()
