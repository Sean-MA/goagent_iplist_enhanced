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
print "Goagent Iplist Auto-Update Tool version 0.2\n"
try:
  webpage = urllib2.urlopen('http://180.168.97.118:8070/sky/a')
  iplist = webpage.read()
except Exception, e:
    print e
    try:
      webpage = urllib2.urlopen('http://192.168.200.70:8070/sky/a')
      iplist = webpage.read()
    except Exception, e:
        print e  
print "Iplist has been fetched...\n"

#f1 = open('E:\Program Files\goagent-goagent-98eca96\local\proxy.ini', 'r+')
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
print "Update finished...\n"
py_file = 'proxy.py'
os.system('python ' + py_file)
