# from sqlite to postgresql
import os
import psycopg2
import sqlite3

def get_connection():
  dsn = os.environ.get('DATABASE_URL')
  return psycopg2.connect(dsn)
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

'''
CREATE TABLE if not exists pos (
              STCD text PRIMARY KEY,
              RVNM text,
              STNM text,
              FRZ text,
              GRZ text,
              WRZ text,
              MAXZ text)

CREATE TABLE if not exists dyna (
              STCD text,
              DATE text,
              Q text,
              YZ text,
              Z text,
              WPTN text,
              PRIMARY KEY(STCD, DATE)
              )
'''

def chk_row(s1, s2, s3, s4):
  '''
  主要４項目のいずれが数字であればTrue
  '''
  if chk_digit(s1) or (chk_digit(s2) and s2!="0.00") or chk_digit(s3) or chk_digit(s4):
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
  

conn1 = sqlite3.connect('example1.db')
conn2 = get_connection()
c1 = conn1.cursor()
c2 = conn2.cursor()

skipcnt = 0
try:
  loop = True
  while loop:
    loop = False
    #for row in c.execute("SELECT * FROM dyna where DATE='1961-02-13 09:00'"):
    #for row in c1.execute("SELECT * FROM dyna where STCD='61802800'"):
    rows = c1.execute("SELECT * FROM dyna limit 10000").fetchall()
    for row in rows:
      loop = True
      flg = chk_row(row[2], row[3], row[4], row[5])
      if flg:
        if skipcnt > 0:
          print("skiped " + str(skipcnt) + " rows")
          skipcnt=0
        print(row, end="")
        try:
          q2 ='''
          INSERT INTO dyna VALUES (%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING          
          '''
          c2.execute(q2, row)
          print("...insert", end="")
        #except psycopg2.errors.UniqueViolation:
        #  # 主キー重複を無視
        #  print("...pass")
        #  pass
        except Exception as e:
          print("...error")
          raise(e)
        else:
          print("...done")
      else:
        #print("...skip")
        skipcnt+=1
      c1.execute('delete from dyna where stcd=? and date=?', (row[0], row[1]))
    conn2.commit()
    conn1.commit()
finally:
  conn1.close()
  conn2.close()

'''
cur.execute('SELECT * FROM dyna')
'''
