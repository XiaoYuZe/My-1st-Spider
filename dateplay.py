a = datetime.datetime.now().strftime('%Y-%m-%d')
b = datetime.datetime.now()
e = datetime.datetime.now()+datetime.timedelta(-2)
c = datetime.date.today()+datetime.timedelta(-2)
d = (datetime.date.today()+datetime.timedelta(-2)).strftime('%Y-%m-%d')
#print 'Now is %s' %a
print a
print b
print e
print c,type(c)
print d,type(d)
#print a ==pub_date