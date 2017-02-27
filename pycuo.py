#!/usr/bin/env Python
# coding=utf-8
import queue
import threading
from prettytable import PrettyTable
from optparse import OptionParser
import lib.http_request
import lib.preg
import lib.thread
import lib.file_method
import lib.Queue_class
from module.scan import *
Thread = threading.Thread
Queue = queue.Queue()
Domain_Result=[]
req_content = PrettyTable(['HOST','TITLE','Server','Status_Code'])
domain_content = PrettyTable(['Domain','HOST','TITLE','SERVER','ADDRESS'])
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
        urls = lib.file_method.read_file_lines(options.dict,'.'+options.url)
        socket.timeout=options.timeOut
        lib.Queue_class.Load_Queue(Queue,urls)
        Threads = lib.thread.Load_Thread(options.thread,Scan_DNS,Queue,Domain_Result)
        lib.thread.Start_Thread(Threads,'Scan_DNS')
        for result in Domain_Result:
            domain_content.add_row([result['Domain'],result['HOST'],result['TITLE'],result['SERVER'],result['ADDRESS']])
            pass
        print(domain_content)
        HOST_LIST = []
        for host in Domain_Result:
            HOST_LIST.append(host['HOST'])
        lib.Queue_class.Load_Queue(Queue,HOST_LIST)
        opt = [options.http_timeOut,options.port]
        Threads = lib.thread.Load_Thread(options.thread,Scan_Port,opt,Queue,req_content)
        lib.thread.Start_Thread(Threads,'Scan_Port')
        print(req_content)
    else:
        print('You have not entered a domain name.')
        exit()
if __name__ == '__main__':
    main()