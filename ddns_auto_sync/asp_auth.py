#从页面提取__VIEWSTATE和__VIEWSTATEGENERATOR，并合并到postdict中
import re

class Asp_auth:
    def __init__(self):
        self.aspdict={}
    def get_asp_auth(self,pagetxt=''):
        re_viewstate=re.compile('__VIEWSTATE.*value="([^"]+)"')
        re_viewstategenerator=re.compile('__VIEWSTATEGENERATOR.*value="([^"]+)"')
        try:
            self.aspdict['__VIEWSTATE']=re_viewstate.search(pagetxt).group(1)
            self.aspdict['__VIEWSTATEGENERATOR']=re_viewstategenerator.search(pagetxt).group(1)
            #print('asp验证码入手！')
        except re.error:
            print('没找到asp验证参数！')

    def set_asp_auth(self,postdict={}):
        return dict(self.aspdict,**postdict)
    
# #test        
# with open('page.html','r') as testf:
#     postdict={}
#     print(get_asp_auth(testf.read(),postdict))