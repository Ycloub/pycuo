import threading
def Load_Thread(thread_count,method,*args):
    Thread_List =[]
    for x in range(thread_count):
        Thread_List.append(threading.Thread(target=method,args=args))
    print('[*]Threading Loader Success ...')
    return Thread_List
def Start_Thread(Thread_List,Explain=''):
    print('[*]'+Explain+' All threads execute start...')
    for thread in Thread_List:
            thread.setDaemon(True)
            thread.start()
    for thread in Thread_List:
        thread.join()
    print('[*]'+Explain+' All threads execute end....')