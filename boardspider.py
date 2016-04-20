#!/usr/bin/env python
# -*- coding='utf-8' -*-
import os,sys
reload(sys)
sys.setdefaultencoding('utf8')
#print sys.getdefaultencoding()
import requests

from bs4 import BeautifulSoup

ah_main = "http://www.ahcourt.gov.cn"
mainpage ="http://www.ahcourt.gov.cn/sitecn/ahfy/index.html"
pagedown = requests.get(mainpage)
#print pagedown.content
#pagedownbs = BeautifulSoup(pagedown.content,'html5lib')
pagedownbs = BeautifulSoup(pagedown.content,'html5lib')
#print pagedownbs.find_all('script')[-2]['src']
ah_court_sub = pagedownbs.find_all('script')[-2]['src']
ah_target = ah_main + ah_court_sub
#print ah_target
ahcourt_net = requests.get(ah_target)
ah_court_bs = BeautifulSoup(ahcourt_net.text,'html5lib')
#print ah_court_bs.find_all('dd')[-1].a['href'], ah_court_bs.find_all('dd')[-1].text
for i in range(len(ah_court_bs.find_all('dd'))):
	if ah_court_bs.find_all('dd')[i].a != None:
		print ah_court_bs.find_all('dd')[i].a['href'], ah_court_bs.find_all('dd')[i].text
	else:
		print ah_court_bs.find_all('dd')[i].a ,'This court has no webpages'






# print pagedownbs.title.text
# print pagedownbs.title
# print pagedownbs.a.text.encode('utf-8','ignore')
# for i in range(9):
# 	f = open('westry.txt','w+')
# 	f.write(pagedownbs.text+str(i))
# 	f.close()
# 	i += 1



# alink = pagedownbs.find_all('a')
# for i in range(len(alink)):
# 	print alink[i].text
