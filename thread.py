#python中与线程相关的库有_thread 和 threading两个库。第一个提供了低级别的，原始的线程以及简单的锁，相比threading模块的功能
#还是有限的。threading模块除了包含_thread模块中的所有方法之外。还有许多功能。
# import threading
# import time
#
# exitFLag=0
#
#
# class MyThread(threading.Thread):
#     def __init__(self, ThreadID , name,delay):
#         threading.Thread.__init__(self)
#         self.ThreadID=ThreadID
#         self.name=name
#         self.delay=delay
#
#     def run(self):
#         print("开始线程："+self.name)
#         threadLock.acquire()
#         print_time(self.name,self.delay,3)
#         # print("退出线程："+self.name)
#         threadLock.release()
#
# def print_time(threadName,delay,counter):
#     while counter:
#         if exitFLag:
#             threadName.exit()
#         time.sleep(delay)
#         print("%s %s"%(threadName,time.ctime(time.time())))
#         counter-=1
#
# threadLock=threading.Lock()
# thread=[]
#
# thread1=MyThread(1,"thread1",1)
# thread2=MyThread(2,"thread2",1)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
# print("退出主线程")





#队列 python中的队列模块中提供了同步的，线程安全的队列类，包括FIFO队列，LIFO队列和优先级队列。这些队列都实现了锁，能够在多线程中
#直接使用，可以使用队列来实现线程之间的同步。
import queue
import threading
import time

exitFlag=0

class myThread(threading.Thread):
    def __init__(self,ThreadId,name,que):
        threading.Thread.__init__(self)
        self.ThreadId=ThreadId
        self.name=name
        self.que=que

    def run(self):
        print("开始线程")
        process_data(self.name,self.que)
        print("退出线程")


def process_data(threadName,que):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data=que.get()
            queueLock.release()
            print("%s processing %s"%(threadName,data))
        else:
            queueLock.release()
        time.sleep(1)


threadList=["Thread1","Thread2","Thread3"]
nameList=["one","two","three","four","five"]
queueLock=threading.Lock()
workQueue=queue.Queue(10)
threads=[]
threadId=1

for tName in threadList:
    thread=myThread(threadId,tName,workQueue)
    thread.start()
    threads.append(thread)
    threadId+=1


queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag=1

for t in threads:
    t.join()
print("退出主线程")





