#如果想要加扩展功能。
def new_function(opt1,opt2,Queue):
    while True:
        if Queue.empty():
            break
        # Other code ....
        job = Queue.get()
#在运行main函数中添加
#Threads = lib.thread.Load_Thread(线程数量,函数名称,参数1,参数2,参数3,...,Queue)
#lib.thread.Start_Thread(Threads,'new_function')
#启动线程