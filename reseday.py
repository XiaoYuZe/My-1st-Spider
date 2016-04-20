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
# target page   http://www.live.chinacourt.org/fygg.shtml
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"}
date_input = raw_input('Input year month day u want:')
print date_input
cnnt = pyodbc.connect('DRIVER={SQL Server};SERVER=121.42.41.188;DATABASE=CourtNotice;UID=zhangxiaogang;PWD="20p2#NAs}123')
cursor = cnnt.cursor()

params={
		"start":1,
		"limit":16,
		"wd":"rmfybulletin",
		"list[0]":"bltntype:"+''
		}
r = requests.post("http://rmfygg.court.gov.cn/psca/lgnot/solr/searchBulletinInterface.do?callback=?", data=params)

# print type(json.loads(r.content[2:-1])['objs'])
# print r.content
content_dict = json.loads(r.content[2:-1])['objs']
content_fin = json.loads(r.content[2:-1])['objs'][1]#.encode('utf8')
link_id = content_fin['id']
crt_name = content_fin['courtcode']
rel_prn = content_fin['party2']
pub_date = content_fin['publishdate']
blt_type = content_fin['bltntypename']
blt_content = content_fin['content']
sql = "INSERT INTO bltin VALUES ('%s','%s','%s','%s','%s','%s')" %(link_id, crt_name, rel_prn, pub_date, blt_type, blt_content)

print pub_date
print pub_date==date_input
# print rel_prn#,type(pub_date),type(blt_type),type(blt_content)
# print crt_name,rel_prn,pub_date,blt_type,blt_content
# cnnt.execute(sql)
# cnnt.commit()