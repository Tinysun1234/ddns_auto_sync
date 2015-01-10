'''
取得公网IP地址
'''

import urllib.request
import re

class Public_ip_checker:
    def get_public_ip(self):
        page=urllib.request.urlopen('http://1111.ip138.com/ic.asp').read()
        m=re.search(r'\d+\.\d+\.\d+\.\d+',str(page))
        if m:
            return m.group(0)
        else:
            return None

            
#test
##print(get_public_ip())
