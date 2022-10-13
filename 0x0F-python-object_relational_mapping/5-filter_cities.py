#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db=MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                        db=sys.argv[3], port=3306)

    C=db.cursor()
    C.execute("SELECT cities.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name = %s;", (sys.argv[4],))
    states = C.fetchall()

    print(", ".join([state[0] for state in states]))
