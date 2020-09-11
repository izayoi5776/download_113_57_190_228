# json to sqlite
# use sqlite here, for sql.js read future

import sqlite3
import json
import glob
import os

def db_create(c):
  # Create table
  '''
  table pos       位置表
    STCD    text  pk
    RVNM    text  河名
    STNM    text  站名
    FRZ     text  设防水位
    GRZ     text  保证水位
    WRZ     text  警戒水位
    MAXZ    text  大概是历史最高水位
  
  table dyna      动态数据表
    STCD    text  pk
    DATE    text  数据检索日时 "yyyy-mm-dd hh:00"
    Q       text  流量
    YZ      text  比昨日+涨-落
    Z       text  水位
    WPTN    text  水势。4降，5升，6平

  注意
    数字位置还可以是空，--，带有(入)(出)和<br>，缺测

  '''
  c.execute('''CREATE TABLE if not exists pos (
              STCD text PRIMARY KEY,
              RVNM text,
              STNM text,
              FRZ text,
              GRZ text,
              WRZ text,
              MAXZ text)
            ''')
  c.execute('''CREATE TABLE if not exists dyna (
              STCD text,
              DATE text,
              Q text,
              YZ text,
              Z text,
              WPTN text,
              PRIMARY KEY(STCD, DATE),
              FOREIGN KEY(STCD) REFERENCES pos(STCD)
              )
            ''')
  conn.commit()


def db_insert_dyna(c, row):
  try:
    c.execute('INSERT INTO dyna VALUES (?,?,?,?,?,?)', row)
  except sqlite3.IntegrityError as e:
    # 主キー重複はSKIP
    pass
  except sqlite3.Error as e:
    print("An error occurred:", e.args[0])


def db_read(c):
  for row in c.execute('SELECT * FROM dyna'):
    print(row)

def json_onefile(c, conn, filename):
  with open(filename) as f:
    j = json.load(f)
    DATE = j["date"]
    for r in j["rows"]:
      if chk_row(r["Q"], r["YZ"], r["Z"], r["WPTN"]):
        db_insert_dyna(c, (r["STCD"], DATE, r["Q"], r["YZ"], r["Z"], r["WPTN"]))
      if chk_row(r["Q1"], r["YZ1"], r["Z1"], r["WPTN1"]):
        db_insert_dyna(c, (r["STCD1"], DATE, r["Q1"], r["YZ1"], r["Z1"], r["WPTN1"]))
  conn.commit()

def chk_row(s1, s2, s3, s4):
  '''
  主要４項目のいずれが数字であればTrue
  '''
  if chk_digit(s1) or chk_digit(s2) or chk_digit(s3) or chk_digit(s4):
    return True
  else:
    return False

def chk_digit(s):
  '''
  非空、先頭文字が数字ならTrue
  '''
  if s!="" and s[0].isdigit():
    return True
  else:
    return False

# ----------- MAIN ----------------

conn = sqlite3.connect('example.db')
c = conn.cursor()
db_create(c)
for filename in glob.glob("json2/*.json"):
  print(filename, end="")
  json_onefile(c, conn, filename)
  os.remove(filename)
  print("...done")
#db_read(c)
conn.close()


