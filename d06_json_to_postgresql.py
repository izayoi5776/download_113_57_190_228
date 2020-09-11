# from json to postgresql
import os
import psycopg2
import json
import glob

'''
  table dyna      动态数据表
    STCD    text  pk
    DATE    text  数据检索日时 "yyyy-mm-dd hh:00"
    Q       text  流量
    YZ      text  比昨日+涨-落
    Z       text  水位
    WPTN    text  水势。4降，5升，6平

  注意
    数字位置还可以是空，--，带有(入)(出)和<br>，缺测

CREATE TABLE if not exists dyna2 (
              STCD text,
              DATE text,
              Y char(4),
              M char(2),
              D char(2),
              H char(2),
              Q text,
              YZ text,
              Z text,
              WPTN text,
              PRIMARY KEY(STCD, DATE)
              );

'''

def get_connection():
  dsn = os.environ.get('DATABASE_URL')
  return psycopg2.connect(dsn)

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

def db_insert_dyna(c, row):
  q2 ='''
  INSERT INTO dyna2 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING          
  '''
  c.execute(q2, row)

def devide_date(DATE):
  return DATE[0:4], DATE[5:7], DATE[8:10], DATE[11:13]

def json_onefile(c, conn, filename):
  with open(filename) as f:
    j = json.load(f)
    DATE = j["date"]
    for r in j["rows"]:
      if chk_row(r["Q"], r["YZ"], r["Z"], r["WPTN"]):
        val = (r["STCD"], DATE) + devide_date(DATE) + (r["Q"], r["YZ"], r["Z"], r["WPTN"])
        #print("val=" + str(val))
        db_insert_dyna(c, val)
      if chk_row(r["Q1"], r["YZ1"], r["Z1"], r["WPTN1"]):
        val = (r["STCD1"], DATE) + devide_date(DATE) + (r["Q1"], r["YZ1"], r["Z1"], r["WPTN1"])
        db_insert_dyna(c, val)
  conn.commit()


if __name__ == "__main__":
  try:
    conn = get_connection()
    c = conn.cursor()

    for filename in glob.glob("json2/*.json"):
      print(filename, end="")
      json_onefile(c, conn, filename)
      os.remove(filename)
      print("...done")

  finally:
    conn.close()
