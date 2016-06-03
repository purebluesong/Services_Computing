#coding=utf-8
import xmlrpclib

week_en =['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
gan = [u'甲', u'乙', u'丙', u'丁', u'戊', u'己', u'庚', u'辛', u'壬', u'癸']
zhi = [u'子', u'丑', u'寅', u'卯', u'辰', u'巳', u'午', u'未', u'申', u'酉', u'戌', u'亥']
yue = [u'正', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九', u'十', u'十一', u'腊',]

#i have to admit that xml-rpc is shit 
proxy = xmlrpclib.ServerProxy("http://localhost:8000/")
while(raw_input("continue?(Y/n)") in ["Y", "y"]):
    year = int(raw_input("year: "))
    month = int(raw_input("month:"))
    day = int(raw_input("day:  "))
    date = proxy.nextdate(year, month, day)
    print date['year'], 'month', date['month'], 'day', date['day'], week_en[date['week']]
    print gan[date['lunar_year']%10]+zhi[date['lunar_year'] % 12], u'年'
    print yue[date['lunar_month']], u'月'
    print date['lunar_day'], u'日'
