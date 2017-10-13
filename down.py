#!/usr/bin/env python
# -*- conding:utf-8 -*-
__Author__ = "Yasin Li"

from urllib import request
url = 'http://jn.58.com/searchjob/pve_5594_1/?key=%E9%94%80%E5%94%AE&cmcskey=%E9%94%80%E5%94%AE&final=1&jump=2&specialtype=gls&jlabtest=&-3=H&param8616=0'

print (url)
req = request.Request(url)
print (req)

res_data = request.urlopen(req)
res = res_data.read()
print (res)