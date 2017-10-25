### python3实现多线程的方法

python3通过以下两个模块实现多线程：

_thread

threading(推荐使用)

1：通过_thread的start_new_thread(function, args, kwargs=None)方法来实现更

**该方法接受一个方法作为线程的执行体，来实现多线程**

案例如下：

```python
#!/usr/bin/python3
import _thread
import time

def print_time( threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

try:
    _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
    _thread.start_new_thread( print_time, ("Thread-2", 3, ) )
except:
    print ("Error")

while 1:
    pass
```

程序运行结果如下：

```
Thread-1: Tue Oct 24 16:55:41 2017
Thread-2: Tue Oct 24 16:55:42 2017
Thread-1: Tue Oct 24 16:55:43 2017
Thread-1: Tue Oct 24 16:55:45 2017
Thread-2: Tue Oct 24 16:55:45 2017
Thread-1: Tue Oct 24 16:55:47 2017
Thread-2: Tue Oct 24 16:55:48 2017
Thread-1: Tue Oct 24 16:55:49 2017
Thread-2: Tue Oct 24 16:55:51 2017
Thread-2: Tue Oct 24 16:55:54 2017
```

2：Python3 通过两个标准库 _thread 和 threading 提供对线程的支持。

- _thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的。
- threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：
- threading.currentThread(): 返回当前的线程变量。
- threading.enumerate(): 
  返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
- threading.activeCount(): 
  返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

  除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:

- run(): 用以表示线程活动的方法。
- start():启动线程活动。
- join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 
  方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
- isAlive(): 返回线程是否活动的。
- getName(): 返回线程名。
- setName(): 设置线程名。

通过threading创建线程的方法为：通过继承threading.Thread来创建一个新的类，调用其start方法启动该线程

实现代码如下：

```python
import threading
import time
exitFlag = 0
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

```

