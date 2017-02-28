import requests
import time
print('None one test ...')
currentTime = time.time()
urlLists=['www.masterchat.cn', 'www.pkuph.cn', 'www.shikee.com', 'www.biyao.com', 'www.kaixinyin.com', 'www.weibo.com', 'p4.qhimg.com', 'zhongce.360.cn', 'www.qdpme.com', 'yingyan.360.cn', 's.360.cn', 'www.ikang.com', 'www.tasly.com', 'zhuji.360.cn', 'www.wanxue.cn', 'www.qiakr.com', 'www.fx678.com', 'www.iliangcang.com', 'www.33m.com','www.01.cn', 'bobao.360.cn', 'www.huaji.com', 'www.zlcf.com', 'www.iwjw.com', 'www.wepiao.com', 'tjnu.edu.cn', 'www.idc18.net','www.upg.cn', 'www.youzu.com', 'webscan.360.cn', 'www.homeinns.com', 'www.xueda.com', 'www.willshop.cn', 's11.cnzz.com', 'www.dnion.com']
print('[*]elements is :' + str(len(urlLists)))
def p(url,number):
    try:
        req = requests.get('http://'+url,timeout=5)
    except:
        print('[*]'+ url)
        return 1
    print(str(number)+'=>' +req.encoding )
for url in urlLists:
    p(url,urlLists.index(url))
print(time.time() - currentTime)