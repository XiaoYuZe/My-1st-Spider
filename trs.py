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

cnnt = pyodbc.connect('DRIVER={SQL Server};SERVER=121.42.41.188;DATABASE=CourtNotice;UID=zhangxiaogang;PWD="20p2#NAs}123')
cursor = cnnt.cursor()
# try:
# 	cursor.execute('CREATE TABLE crt_blt (crt_name nvarchar(100), rld_prn nvarchar(500), pub_date nvarchar(500), blt_type nvarchar(100), blt_content nvarchar(5000')
# 	cnnt.commit()
# 	cnnt.close()
# 	print 'table created'
	
# except:
# 	print 'table exist'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"}

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
			link_id = content_fin['id']
			crt_name = content_fin['courtcode']
			rel_prn = content_fin['party2']
			pub_date = content_fin['publishdate']
			blt_type = content_fin['bltntypename']
			blt_content = content_fin['content']
			sql = "INSERT INTO bltin VALUES ('%s','%s','%s','%s','%s','%s')" %(link_id, crt_name, rel_prn, pub_date, blt_type, blt_content)
			cnnt.execute(sql)
			cnnt.commit()
			# print k+1,crt_name,rel_prn,pub_date,blt_type,blt_content
			print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~This is '+ str(n) + ' page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
	else:
		print 'Home Total is '+str(n)+ ' page'
		break
