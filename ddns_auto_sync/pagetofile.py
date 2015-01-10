'''
将抓取的网页按不同编码解码和存盘，一般调试用
'''

def ptf(resp,filecoding='gb2312',pagecoding='gb2312',filename='page.html'):
    try:
        with open(filename,'w',-1,filecoding) as pagef:
            print(resp.read().decode(pagecoding),file=pagef)
            print('Page dumps to '+filename+' successful!')
    except IOError as e:
        print('Page dump to '+filename+' failed!')
        print(str(e))
                