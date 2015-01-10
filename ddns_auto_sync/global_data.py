'''
运行数据。88ip.cn的用户名/密码放在：../ddns_passwd.txt 中，第一行用户名，第二行密码
'''

class Global_data():
    def __init__(self):
        self.url_welcome='http://88ip.cn/'
        self.url_login='http://88ip.cn/login.aspx'
        self.url_admin='http://88ip.cn/Users/Loged/DomainList.aspx'
        self.url_logout='http://88ip.cn/default.aspx'
        #new_public_ip changes at runtime
        self.new_public_ip='1.1.1.1'
        self.domain_name='home-desktop'
        self.hder={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0',
              'Referer':'http://88ip.cn/',
              'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
              'Accept-Language':'en-US,en;q=0.5',
              'Accept-Encoding':'gzip, deflate',
              'Connection':'keep-alive'
              }
        with open('../ddns_passwd.txt','r') as fdata:
            self.postdict_login={'m_szUserName':fdata.readline(),
                    'm_szUserPwd':fdata.readline(),
                    'm_btnLogin':'登录(Alt+L)'}
        
        self.postdict_fixip={'DomainName':'',
                        'SuffixName':'.88ip.cn',
                        'restype':'A',
                        'domainindex':'0',
                        'resindex':'0',
                        'resname':self.domain_name,
                        'resvalue':self.new_public_ip,
                        'btn':'修改'}
