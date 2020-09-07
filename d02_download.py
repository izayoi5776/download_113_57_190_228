# d02_download.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import json
from datetime import timedelta
from datetime import datetime
import os

# 2020-09-04 08:00
script2 = '''
  var date = $("#start").val() + " " + $("#starth").val();
  return date;
'''

# download 1 date
# return json
def download(driver, fromdate):
  # start 1865-01-27 08:00 汉口
  # 2009-04-01 09:00 
  mydate = "var date = '" + fromdate + "';"
  script3 = '''
    return $.ajax({
        type: 'get',
        url: '/Web/Report/GetRiverData',
        async: false,
        data: {
            date: date
        },
        success: function (d) {
            console.log(d)
            return d;
        }
    });
  '''
  return driver.execute_script('javascript:' + mydate + script3 + ';')

def getjson(driver, fromdate, filename):
  '''
  get json from server
  add parameter date
  save to file
  '''
  myjson = {
    "date" : fromdate,
    "rows" : download(driver, fromdate)["rows"]
  }
  with open(filename, 'w') as f:
    json.dump(myjson, f, indent=2, ensure_ascii=False)


#with webdriver.Chrome() as driver: # なぜかchromeだめ
with webdriver.Firefox() as driver:
  wait = WebDriverWait(driver, 10)
  try:
    driver.get("http://113.57.190.228:8001/web/Report/RiverReport")
    time.sleep(20)
  except:
    time.sleep(20)

  # start 1865-01-27 08:00 汉口
  #loopdt = datetime.fromisoformat('1865-01-01T00:01:00')
  loopdt = datetime.fromisoformat('1925-06-01T00:01:00')
  onehour = timedelta(hours=1)
  JSONPATH = "json"
  os.makedirs(JSONPATH, exist_ok=True)
  while loopdt < datetime.now():
    fromdate = loopdt.strftime("%Y-%m-%d %H:00")
    filename = JSONPATH + "/" + fromdate.replace("-", "").replace(" ", "_").replace(":", "") + '.json'
    print(filename, end="")
    if(os.path.isfile(filename)):
      print(".... SKIP")
    else:
      getjson(driver, fromdate, filename)
      print(".... DOWNLOADED")
      #time.sleep(1)

    loopdt += onehour

  print("end")
  time.sleep(10)
