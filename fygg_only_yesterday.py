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

reload(sys)
sys.setdefaultencoding('utf8')
# target page   http://www.live.chinacourt.org/fygg.shtml
#--server connect ,Database table has established
cnnt = pyodbc.connect('DRIVER={SQL Server};SERVER=121.42.41.188;DATABASE=CourtNotice;UID=zhangxiaogang;PWD="20p2#NAs}123')
cursor = cnnt.cursor()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"}
#error count for ValueError:'No JSON object could be decoded' 
#output is the result divider
err_count = 0
output = 0

now = datetime.date.today()
# 'the day before yesterday'
yesd = (now+datetime.timedelta(-1)).strftime('%Y-%m-%d')
# when the subloop find the yesd,bre_condition will be True,big loop break
bre_condition = False
f = open('E:\My Spider\log\\'+datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')+'.txt','w')
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
				#print pub_date
				if pub_date == yesd:
					
					try:
						cnnt.execute(sql)
						cnnt.commit()
						f.write('~~'+'NEW'+'~~This is '+str(n)+' page~~'+str(k+1)+' line'+'link'+str(link_id)+"is NEW!"+' Saved '+'~~~~~'+'\n')
						print '~~'+'NEW'+'~~This is '+str(n)+' page~~'+str(k+1)+' line'+'link'+str(link_id)+"is NEW!"+' Saved '+'~~~~~~~~~~'
					except:
						f.write( '~~'+'OLD'+'~~This is '+str(n)+' page~~'+str(k+1)+'~~~'+str(link_id)+' already exist'+'~~~~~'+'\n')
						print '~~'+'OLD'+'~~This is '+str(n)+' page~~'+str(k+1)+'~~~'+str(link_id)+' already exist'+'~~~~~~~~~'
						continue
					# print k+1,crt_name,rel_prn,pub_date,blt_type,blt_content
					# print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~This is '+ str(n) + ' page~~~~~~~~~~~' +str(k+1)+ '~~~~~~~~~~~~'+str(link_id)+'already exist'+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

					bre_condition = True
					output = 1
				
				else:
					if n < 100: #print 'no need data'
						continue
					else:
						# f.write(yesd+' website has no data update'+'\n')
						# print yesd+' website has no data update'
						bre_condition = True
						break
					
								
			
		except:
			err_count +=1
			f.write('Error Unexpected times? '+str(err_count)+'\n')
			print 'Error Unexpected times? '+str(err_count)
			continue
	else:
		# output is the result divider
		if output==1:
			f.write('Update '+yesd+' Data'+'\n')
			print 'Update '+yesd+' Data'
			break
		else:
			f.write(yesd+' website has no data update'+'\n')
			print yesd+' website has no data update'
			break
f.close()



