#! /usr/bin/env python
#coding:utf-8

import sys
import re
import urllib2
import urllib
import requests
import cookielib

## 这段代码是用于解决中文报错的问题  
#reload(sys)  
#sys.setdefaultencoding("utf8")  
#####################################################
print "Goagent Iplist Auto-Update Tool version 0.1\n"
signin_url = "http://www.firefoxfan.com/wp-login.php"

logininfo = {"log": "ma.xiaoyuan.mail@gmail.com",
             "pwd": "maxiaoyuan1234",
             "wp-submit": "登录"
             }
 
user_agent = ("Mozilla/5.0 (Windows NT 5.1) "
              "AppleWebKit/537.36 (KHTML, like Gecko) "
              "Chrome/41.0.2272.118 Safari/537.36")

post_headers = {"User-Agent": user_agent,
                "Referer": "http://www.firefoxfan.com/wp-login.php"
                }
firefoxfan_session = requests.Session()

login_res = firefoxfan_session.post(signin_url,
                                  data=logininfo,
                                  headers=post_headers,
                                  )
print "Login...\n"
if login_res.status_code == 200:
    print "Login Successfully!\n"
else:
    print login_res.text


from bs4 import BeautifulSoup
webpage = urllib2.urlopen('http://www.firefoxfan.com/firefox-gaogent/goagent-ip.html')
soup = BeautifulSoup(webpage)
f = open('out.txt', 'w')
for anchor in soup.find_all('span', class_ ='crayon-cn'):
    print >> f, anchor.contents
else:
    f.close()
import re
f1 = open('out.txt')
f2 = open('out1.txt','w')
f2.close()
f2 = open('out1.txt','r+')
for s in f1.readlines():
    f2.write(s.replace("[u'",''))
f1.close()
f2.close()
f1 = open('out1.txt')
f2 = open('out2.txt','w')
f2.close()
f2 = open('out2.txt','r+')
for s in f1.readlines():
    f2.write(s.replace("']\n",'|'))
f2.seek(-1,2)
f2.write('\n')
f2.close()
f1.close()

f2 = open('out2.txt','r+')
iplist = f2.read()
f2.close()
f1 = open('proxy.ini', 'r+')
source = f1.read()
pos = source.find("google_cn",source.find("[iplist]"))+len("google_cn")
pos1 = source.find("google_hk",pos)
source = source[:pos] + " = " + iplist + source[pos1:]
pos = source.find("google_hk",source.find("[iplist]"))+len("google_hk")
pos1 = source.find("google_talk",pos)
source = source[:pos] + " = " + iplist + source[pos1:]
pos = source.find("google_talk",source.find("[iplist]"))+len("google_talk")
pos1 = source.find("[",pos)
source = source[:pos] + " = " + iplist + source[pos1:]
f1.seek(0,0)
f1.truncate()
f1.write(source)
f1.close()

import os
os.remove('out.txt')
os.remove('out1.txt')
os.remove('out2.txt')
print "Update finished..."
raw_input(unicode('按任意键启动goagent...','utf-8').encode('gbk'))
os.system(r'"goagent.exe"')
