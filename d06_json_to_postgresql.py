# from json to postgresql
import os
import psycopg2
import json
import glob
import re

'''
CREATE TABLE if not exists dyna (
              STCD  text,               -- PK 水文站编码
              DATE  text,               -- PK 数据检索日时 "yyyy-mm-dd hh:00"
              Y     char(4),            -- DATE分解版检索用
              M     char(2),            -- DATE分解版检索用
              D     char(2),            -- DATE分解版检索用
              H     char(2),            -- DATE分解版检索用
              Q     decimal(9,2),       -- 流量。数字以外被删除，出入都有时放出
              QIN   decimal(9,2),       -- Q分解版。出入都有时放入，其他时候空
              YZ    decimal(9,2),       -- 比昨日+涨-落
              Z     decimal(9,2),       -- 水位
              WPTN  char(1),            -- 水势。4降，5升，6平
              PRIMARY KEY(STCD, DATE)
              );
  注意
    数字位置还可以是空，--，带有(入)(出)和<br>，缺测

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
  非空、先頭文字が数字、＋－ならTrue
  '''
  ret = False
  if s!="":
    if s[0].isdigit():
      ret = True
    elif (s[0]=='+' or s[0]=='-') and len(s)>1 and s[1].isdigit():
      ret = True

  return ret

def divide_q(s):
  '''
  数字项目分拆

  '''
  ret_in = None # 如果拆分得到（入）
  ret_ot = None 
  ptn_in = ".*?([+-]?[\d\.]+)\(入\)"
  ptn_ot = ".*?([+-]?[\d\.]+)\(出\)"
  ptn    = "[+-]?[\d.]+"
  if chk_digit(s):
    # 不会是：空，--，缺测
    # 可能是：123(出)，45.6（入）<br>67.8(出)
    re_in = re.match(ptn_in, s)
    re_ot = re.match(ptn_ot, s)
    if re_in:
      ret_in = re_in.group(1)
    if re_ot:
      ret_ot = re_ot.group(1)
    if not re_ot:
      ret = re.findall(ptn, s)
      if len(ret) == 0:
        print("[WARN] 从 %s 中没能取出数字", s)
      elif len(ret) > 1:
        print("[WARN] 从 %s 中取出超过1个数字 %s", s, ret)
      else:
        ret_ot = ret[0]
  return (ret_ot, ret_in)

def convert_float(s):
  '''
  字符串转换为浮点数
  '''
  ret = None
  try:
    ret = float(s)
  except:
    pass
  return ret

def db_insert_dyna(c, row):
  q2 ='''
  INSERT INTO dyna VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING
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
        val = (r["STCD"], DATE) + devide_date(DATE) + divide_q(r["Q"]) + (convert_float(r["YZ"]), convert_float(r["Z"]), r["WPTN"])
        #print("val=" + str(val))
        db_insert_dyna(c, val)
      if chk_row(r["Q1"], r["YZ1"], r["Z1"], r["WPTN1"]):
        val = (r["STCD1"], DATE) + devide_date(DATE) + divide_q(r["Q1"]) + (convert_float(r["YZ1"]), convert_float(r["Z1"]), r["WPTN1"])
        db_insert_dyna(c, val)
  conn.commit()


if __name__ == "__main__":
  try:
    conn = get_connection()
    c = conn.cursor()

    for filename in glob.glob("json/*.json"):
      print(filename, end="")
      json_onefile(c, conn, filename)
      os.remove(filename)
      print("...done")

  finally:
    conn.close()
