#!/usr/bin/env python
# -*- coding='utf-8' -*-
import sys
import requests
import selenium
import json
import os
import pyodbc
reload(sys)
sys.setdefaultencoding('utf8')
from bs4 import BeautifulSoup

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=121.42.41.188;DATABASE=ddfe;UID=zhangxiaogang;PWD="20p2#NAs}123')
cursor = cnxn.cursor()
try:
	cursor.execute("create table crt_blt")
	print 'table created'
except:
	print 'table exist'

# court_page = "http://www.live.chinacourt.org/fygg.shtml"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"}
# page_get = requests.get(court_page,headers=headers)
# page_getbs = BeautifulSoup(page_get.content,'html5lib')
# print page_getbs

# params={
		# "start":1,
		# "limit":16,
		# "wd":"rmfybulletin",
		# "list[0]":"bltntype:"+''
		# }
# r = requests.post("http://rmfygg.court.gov.cn/psca/lgnot/solr/searchBulletinInterface.do?callback=?", data=params)
# print json.loads(r.content[2:-1])['objs'][0].get('content') #.decode('utf8').encode('gbk') This is a dict
# print (r.content[2:-1])    This is a str

# Per Page Iteration

# content_dict = json.loads(r.content[2:-1])['objs']
#for k in range(len(content_dict)):
    #print k
# content_fin = json.loads(r.content[2:-1])['objs'][0]#.encode('utf8')
# for i in content_fin:
# 	print i,content_fin[i]
# print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
# crt_name = content_fin['courtcode']
# rel_prn = content_fin['party2']
# pub_date = content_fin['publishdate']
# blt_type = content_fin['bltntypename']
# blt_content = content_fin['content']
# print crt_name,rel_prn,pub_date,blt_type,blt_content

#~~~~~~~~~~~~
# for n in range(1,50):
# 	params={
# 			"start":n,
# 			"limit":16,
# 			"wd":"rmfybulletin",
# 			"list[0]":"bltntype:"+''
# 			}
# 	r = requests.post("http://rmfygg.court.gov.cn/psca/lgnot/solr/searchBulletinInterface.do?callback=?", data=params)



# 	content_dict = json.loads(r.content[2:-1])['objs']
# 	for k in range(len(content_dict)):
# 	    #print k
# 		content_fin = json.loads(r.content[2:-1])['objs'][k]#.encode('utf8')
# 		for i in content_fin:     #display all the message in the dict
# 			print i,content_fin[i]
# 		print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~This is '+ str(n) + ' page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'


#~~~~~~~~~~~~ Test Ok
# for n in range(1,50):
# 	params={
# 			"start":n,
# 			"limit":16,
# 			"wd":"rmfybulletin",
# 			"list[0]":"bltntype:"+''
# 			}
# 	r = requests.post("http://rmfygg.court.gov.cn/psca/lgnot/solr/searchBulletinInterface.do?callback=?", data=params)



# 	content_dict = json.loads(r.content[2:-1])['objs']
# 	for k in range(len(content_dict)):
# 	    #print k
# 		content_fin = json.loads(r.content[2:-1])['objs'][k]#.encode('utf8')
# 		crt_name = content_fin['courtcode']
# 		rel_prn = content_fin['party2']
# 		pub_date = content_fin['publishdate']
# 		blt_type = content_fin['bltntypename']
# 		blt_content = content_fin['content']
# 		print k+1,crt_name,rel_prn,pub_date,blt_type,blt_content
# 		print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~This is '+ str(n) + ' page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'


# Test Page Max
for n in range(20800,99999999):
	params={
			"start":n,
			"limit":16,
			"wd":"rmfybulletin",
			"list[0]":"bltntype:"+''
			}
	r = requests.post("http://rmfygg.court.gov.cn/psca/lgnot/solr/searchBulletinInterface.do?callback=?", data=params)




	content_dict = json.loads(r.content[2:-1])['objs']
	#print content_dict
	if content_dict != []:
		for k in range(len(content_dict)):
		    #print k
			content_fin = json.loads(r.content[2:-1])['objs'][k]#.encode('utf8')
			crt_name = content_fin['courtcode']
			rel_prn = content_fin['party2']
			pub_date = content_fin['publishdate']
			blt_type = content_fin['bltntypename']
			blt_content = content_fin['content']
			
			print k+1,crt_name,rel_prn,pub_date,blt_type,blt_content
			print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~This is '+ str(n) + ' page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
	else:
		print 'Home Total is '+str(n)+ ' page'
		break

