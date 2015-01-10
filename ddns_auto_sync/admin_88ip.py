'''
获取http://88ip.cn上与DDNS绑定的IP地址;
重新绑定指定IP地址
'''

import urllib.request
import urllib.parse
import http.cookiejar
import re
from asp_auth import Asp_auth 
from global_data import Global_data

class Admin_88ip():
    def __init__(self):
        self.gdata=Global_data()
    def get_registered_ip(self):
        # cookie
        cj = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        
        # get asp auth
        req_welcome = urllib.request.Request(self.gdata.url_login, None, self.gdata.hder)
        resp_welcome = self.opener.open(req_welcome)
        self.aspauthor = Asp_auth()
        self.aspauthor.get_asp_auth(resp_welcome.read().decode('gb2312'))
        
        # login
        postdict_login = self.aspauthor.set_asp_auth(self.gdata.postdict_login)
        postdata_login = urllib.parse.urlencode(postdict_login).encode(encoding='gb2312')
        req_login = urllib.request.Request(self.gdata.url_login, postdata_login, self.gdata.hder)
        self.opener.open(req_login)
        resp_admin = self.opener.open(self.gdata.url_admin)
        return re.search('\d+\.\d+\.\d+\.\d+', resp_admin.read().decode('gb2312')).group(0)
        
    def sync_ip(self,ip):
        self.gdata.postdict_fixip['resvalue']=ip
        #modify ip binding
        postdict_fixip=self.aspauthor.set_asp_auth(self.gdata.postdict_fixip)
        postdata_fixip=urllib.parse.urlencode(postdict_fixip).encode(encoding='gb2312')
        req_admin=urllib.request.Request(self.gdata.url_admin,postdata_fixip,self.gdata.hder)
        self.opener.open(req_admin)
        self.opener.open(self.gdata.url_logout)
    

