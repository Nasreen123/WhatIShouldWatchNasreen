"""
This file connects to the database, and prints the contents.

Replace 'watch' with the name of the database
(Replace host, user, password if appropriate)
Replace 'moviestwo' with the name of the table
"""

import MySQLdb
db = MySQLdb.connect(host="localhost",
                     user="root",
                     password="",
                     db="watch")

#The cursor allows us to execute commands in a database session
#The default cursor returns lists
cur = db.cursor()

cur.execute("SELECT * FROM `moviestwo`")

data = cur.fetchall()

for row in data:
    print row

db.close()
