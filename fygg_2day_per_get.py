#!/usr/bin/env python
# -*- coding='utf-8' -*-
import sys
import requests
import selenium
import json
import os
import pyodbc
import datetime
from bs4 import BeautifulSoup
import logging
logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename= datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')+'.log',
                filemode='w')
reload(sys)
sys.setdefaultencoding('utf8')
# target page   http://www.live.chinacourt.org/fygg.shtml
#--server connect ,Database table has established
cnnt = pyodbc.connect('DRIVER={SQL Server};SERVER=121.42.41.188;DATABASE=CourtNotice;UID=zhangxiaogang;PWD="20p2#NAs}123')
cursor = cnnt.cursor()


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"}
#error count for ValueError:'No JSON object could be decoded'
err_count = 0

now = datetime.date.today()
# 'the day before yesterday'
yesd = (now+datetime.timedelta(-2)).strftime('%Y-%m-%d')
# when the subloop find the yesd,bre_condition will be True,big loop break
bre_condition = False
f = open(datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')+'.txt','w')
# start spidering in the range loops,n is the page
for n in range(1,500):
	params={
			"start":n,
			"limit":16,
			"wd":"rmfybulletin",
			"list[0]":"bltntype:"+''
			}
	r = requests.post("http://rmfygg.court.gov.cn/psca/lgnot/solr/searchBulletinInterface.do?callback=?", data=params)

	if bre_condition==False:
		# ValueError status release try
		try:
			content_dict = json.loads(r.content[2:-1])['objs']
			#print content_dict
			#--break condition!
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
					# try for if double data
					if pub_date == yesd:
						
						bre_condition = True
						break
					else:
						try:
							cnnt.execute(sql)
							cnnt.commit()
							print '~~'+'NEW'+'~~This is '+str(n)+' page~~'+str(k+1)+' line'+'link'+str(link_id)+"is NEW!"+' Saved '+'~~~~~~~~~~'
						except:
							print '~~'+'OLD'+'~~This is '+str(n)+' page~~'+str(k+1)+'~~~'+str(link_id)+' already exist'+'~~~~~~~~~'
							continue
						# print k+1,crt_name,rel_prn,pub_date,blt_type,blt_content
						# print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~This is '+ str(n) + ' page~~~~~~~~~~~' +str(k+1)+ '~~~~~~~~~~~~'+str(link_id)+'already exist'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
			
			else:
				print 'Home Total is '+str(n)+ ' page'
				break
		except:
			err_count +=1
			print 'Error Unexpected times? '+str(err_count)
			continue
	else:
		print 'Update From '+str(now)+' to '+ str(yesd)
		break




