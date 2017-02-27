import threading
import queue
# def Load_Thread(thread_count,method,*args):
#     Thread_List =[]
#     for x in range(thread_count):
#         Thread_List.append(threading.Thread(target=method,args=args))
#     print('[*]Threading Loader Success ...')
#     return Thread_List
# def Start_Thread(Thread_List,Explain=''):
#     print('[*]'+Explain+' All threads execute start...')
#     for thread in Thread_List:
#             thread.setDaemon(True)
#             thread.start()
#     for thread in Thread_List:
#         thread.join()
#     print('[*]'+Explain+' All threads execute end....')
# Queue = queue.Queue()
# for x in range(0,200):
#     Queue.put(x)
# sname = 'aa'
# sage  = 18
# hold = 'qqq'
# def pr(sname,sage):
#     while True:
#         if Queue.empty():
#             break
#         print(sname+str(sage)+ '|'+ str(Queue.get()))
#     print('[*]END...')
# for x in range(0,100):
#     Queue.put(x)
# def AAr(hold):
#     while True:
#         if Queue.empty():
#             break
#         print(hold + str(Queue.get()))
#     print('[*]END...')
# TList = Load_Thread(10,pr,sname,sage)
# Start_Thread(TList,'PR')
# TList = Load_Thread(10,AAr,hold)
# Start_Thread(TList,'AAr')
dic = [{'HOST':'111','NAME':'123456'}]
def aa(dic):
        dic.append({'HOST':'aaa','NAME':'789456'})
if __name__ == '__main__':
    aa(dic)
    print(dic)
