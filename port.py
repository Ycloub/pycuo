import requests
import socket
import queue
import os
import re
import threading
from prettytable import PrettyTable
from optparse import OptionParser
Thread = threading.Thread
Queue = queue.Queue()
Domain_Result=[]
req_content = PrettyTable(['HOST','TITLE','Server','Status_Code'])
domain_content = PrettyTable(['Domain','HOST'])
def Load_Queue(queue_opt_list):
    for element in queue_opt_list:
        Queue.put(element)
def Scan_DNS(arg):
    while True:
        if not Queue.empty():
            domain = Queue.get()
            try:
                Host = socket.gethostbyname(domain)
            except:
                    print('[-]PASS ..' + domain)
                    continue
            if(Host):
                Domain_Result.append({'Domain':domain,'HOST':str(Host)})
            else:
                continue
        else:
            exit()
def Load_Thread(thread_count,method,args=''):
    Thread_List =[]
    for x in range(thread_count):
        Thread_List.append(threading.Thread(target=method,args=(args,)))
    return Thread_List
def Start_Thread(Thread_List,Explain=''):
    print('[*]'+Explain+' All threads execute start...')
    for thread in Thread_List:
            thread.setDaemon(True)
            thread.start()
    for thread in Thread_List:
        thread.join()
    print('[*]'+Explain+' All threads execute end....')
def Scan_Port(options):
    #print(options[0])
    while True:
        if not Queue.empty():
            HOST = Queue.get()
            for p in options[1]:
                host = 'http://'+HOST+':'+str(p)
                try:
                    request = requests.get(host,timeout=options[0])
                except:
                    continue
                if request:
                    title_match= '<title>(.*)</title>'
                    try:
                        reGroup = re.search(title_match,request.content.decode('utf-8'))
                        title = reGroup.groups()[0]
                    except:
                        title=''
                    try:
                        server = request.headers['Server']
                    except:
                        server = 'NULL'
                    req_content.add_row([host,title,server,str(request.status_code)])
        else:
            break
def main():
    parser = OptionParser()
    parser.add_option('-u','--url',dest='url',help='Domain to blast.',type='string')
    parser.add_option('-s','--socket_timeout',dest='timeOut',help='Request timeout.',type='int',default=300)
    parser.add_option('-d','--dict',dest='dict',help='Domain dictionary',type='string')
    parser.add_option('-t','--thread',dest='thread',help='Thread count.',type='string',default=10)
    parser.add_option('-b','--banner',dest='banner',default=True,action='store_false',help='No detection banner.')
    parser.add_option('-p','--port',dest='port',default=[80,8080],help='Find the port required by the HTTP service')
    parser.add_option('-k','--httpTimeout',dest='http_timeOut',default=1,help='HTTP request timeout.')
    (options,args)=parser.parse_args()
    if options.port != [80,8080]:
        options.port=options.port.split(',')
    if options.url and  options.dict:
        urls = []
        if os.path.isfile(options.dict):
            try:
                file = open(options.dict,'r')
                for line in file.readlines():
                    line=line.strip()+'.'+options.url
                    urls.append(line)
            except:
                print(options.dict + 'file can not read .')
            finally:
                file.close()
        socket.timeout=options.timeOut
        Load_Queue(urls)
        Threads = Load_Thread(options.thread,Scan_DNS)
        Start_Thread(Threads,'Scan_DNS')
        for result in Domain_Result:
            domain_content.add_row([result['Domain'],result['HOST']])
            pass
        print(domain_content)
        HOST_LIST = []
        for host in Domain_Result:
            HOST_LIST.append(host['HOST'])
        Load_Queue(HOST_LIST)
        opt = [options.http_timeOut,options.port]
        Threads = Load_Thread(options.thread,Scan_Port,opt)
        Start_Thread(Threads,'Scan_Port')
        print(req_content)
    else:
        print('You have not entered a domain name.')
        exit()
if __name__ == '__main__':
    main()