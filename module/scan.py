import lib.http_request
import lib.preg
import socket
import lib.http_request
import json
def Scan_DNS(Queue,Domain_Result):
    while True:
        if not Queue.empty():
            domain = Queue.get()
            try:
                Host = socket.gethostbyname(domain)
            except:
                    #print('[-]PASS ..' + domain)
                    continue
            if(Host):
                hostaddr = getIPaddress(Host)
                request = lib.http_request.url_get('http://'+domain,timeout=5)
                if request:
                    try:
                        content = request.content.decode('utf-8')
                    except UnicodeDecodeError:
                        #print(UnicodeDecodeError.encoding)
                        content = ''
                    title = lib.preg.preg_match_One('<title>(.*)</title>',content)
                    if 'Server' in request.headers:
                        server = request.headers['Server']
                    else:
                        server = None
                    Domain_Result.append({'Domain':domain,'HOST':str(Host),'TITLE':title,'SERVER':server,'ADDRESS':hostaddr})
            else:
                continue
        else:
            exit()
def Scan_Port(options,Queue,req_content):
    while True:
        if not Queue.empty():
            HOST = Queue.get()
            for p in options[1]:
                host = 'http://'+HOST+':'+str(p)
                #print('[*]Scan the ... '+host)
                request = lib.http_request.url_get(host,timeout=options[0])
                if request:
                    title = lib.preg.preg_match_One('<title>(.*)</title>',request.content.decode('utf-8'))
                    if 'Server' in request.headers:
                        server = request.headers['Server']
                    else:
                        server = None
                    req_content.add_row([host,title,server,str(request.status_code)])
        else:
            break
def new_function(opt1,opt2,Queue):
    while True:
        if Queue.empty():
            break
        # Other code ....
        job = Queue.get()
def getIPaddress(ip):
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip='+ip
    req = lib.http_request.url_get(url,timeout=3)
    if hasattr(req,'content'):
        address = json.loads(req.content.decode('utf-8'))
        return address['data']['country']+address['data']['city']+address['data']['isp']
    return None