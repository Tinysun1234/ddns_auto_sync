
import re
#from pagetofile import ptf

def find_ip_in_page(page):
#    ptf(page)
    try:
        return re.search('\d+\.\d+\.\d+\.\d+', page.read().decode('gb2312')).group(0)
    except re.error as e:
        print('IP addr not found:'+str(e))
        return None

            