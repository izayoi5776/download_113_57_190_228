# sqlite件数取得

import sqlite3
import json
import glob
import os



def db_read(c):
  for row in c.execute('SELECT count(*) FROM dyna'):
    print(row)

# ----------- MAIN ----------------

conn = sqlite3.connect('example1.db')
c = conn.cursor()
db_read(c)
conn.close()


