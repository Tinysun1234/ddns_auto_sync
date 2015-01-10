'''
主程序，每120s检查一次公网IP和DDNS绑定IP是否匹配，否则重新绑定DDNS IP
'''

from admin_88ip import Admin_88ip
from public_ip_checker import Public_ip_checker
import time

def gettimenow():
    return time.strftime("%y-%m-%d %H:%M:%S",time.localtime(time.time()))
def getdatenow():
    return time.strftime("%y-%m-%d",time.localtime(time.time()))

with open('log'+getdatenow()+'.txt','a') as logf:
    while(1):
        pipchker=Public_ip_checker()
        ddnsadmin=Admin_88ip()
        pubip=pipchker.get_public_ip()
        regip=ddnsadmin.get_registered_ip()

        if(pubip!=regip):
            print(gettimenow()+' : Re-register ddns ip!',file=logf)
            ddnsadmin.sync_ip(pubip)
            regip=ddnsadmin.get_registered_ip()
            print(gettimenow()+' : Now that...')
            print(gettimenow()+' : Current public ip : '+pubip,file=logf)
            print(gettimenow()+' : Registered ddns ip : '+regip,file=logf) 
        else:
            print(gettimenow()+' : IP Sync: '+pubip,file=logf)
        logf.flush()
        time.sleep(120)
