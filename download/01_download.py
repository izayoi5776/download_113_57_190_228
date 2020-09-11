# coding: UTF-8
import urllib.request, urllib.error
import os
import sys
import time
import datetime
import json

'''
      "STCD": "60105400",   # 表明位置的key
      "RVNM": "长江",       # 江河湖
      "STNM": "寸滩",       # 水文站
      "Z": "173.14",        # 水位
      "WPTN": "4",          # 水势 4降，5升，6平
      "Q": "23000",         # 流量
      "YZ": "-2.01",        # 比昨日+涨-落
      "FRZ": "21.50",       # 设防水位
      "WRZ": "22.80",       # 警戒水位
      "GRZ": "23.94",       # 保证水位
      "MAXZ": "24.59",
'''
def downloadJson(dt):
  '''
  下载dt指定的json，并返回
  '''
  #url = "http://113.57.190.228:8001/Web/Report/GetRiverData?date=2020-07-21+08%3A00"
  url = "http://113.57.190.228:8001/Web/Report/GetRiverData?date=" + urllib.parse.quote_plus(dt.strftime("%Y-%m-%d %H:00"))
  print("url=" + url)
  path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "json")
  os.makedirs(path, exist_ok=True)

  name = os.path.join(path, dt.strftime("%Y-%m-%d_%H_00") + ".json")
  if os.path.exists(name):
    print("skip     " + url + " => " + name)
  else:
    try:
      with urllib.request.urlopen(url) as fp:
        return json.load(fp)

      print("download " + url + " => " + name)
      time.sleep(1)
    except Exception as ex:
      #print("download " + url + " -- FAILED")
      print(ex)



'''
download 
'''
if __name__ == '__main__':
  delta = datetime.timedelta(hours=-1)
  nw = datetime.datetime.today()
  dt = datetime.datetime(nw.year, nw.month, nw.day, nw.hour, 0) # 2020-07-21 21:00:00
  #for i in range(1,100):
  #  print(dt.strftime("%Y-%m-%d %H:00"))
  #  dt = dt + delta
  js = downloadJson(dt+delta)
  print(js)


