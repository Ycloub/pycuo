# import time
# import queue
# Queue = queue.Queue()
# for x in range(100):
#     #print(str(x),end='\r')
#     Queue.put(x)
# print(Queue.get())
# print(Queue.qsize())
# for x in range(10):
#     time.sleep(2)
#     print("Progress {:2.1%}".format(x / 10), end="\r")
import sys
import time

# for i in range(10):
#     sys.stdout.write("\r" + str(i))
#     sys.stdout.flush()
#     time.sleep(1)
txt = '/root/PycharmProjects/pycuo/50.txt'
f = open(txt,'r')
for d in f.readlines():
    d = d.split()
    time.sleep(1)
    print(d,end="\r")