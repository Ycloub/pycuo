# Pycuo
Pycuo(python cora auto)  is a Penetration testing information collection tool.
```
root@Qingxuan:~/PycharmProjects/pycuo# python35 port.py -u sdufe.edu.cn -d 50.txt
[*]Threading Loader Success ...
[*]Scan_DNS All threads execute start...

```
## Extend function
```
def new_function(opt1,opt2,Queue):
    while True:
        if Queue.empty():
            break
        job = Queue.get()
        # current thread job
        # other code ...
```
in the main function add :

Threads = lib.thread.Load_Thread(thread_count,function_name,parameter1,parameter2,parameter3,...,Queue)
lib.thread.Start_Thread(Threads,'function_name')

