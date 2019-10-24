#分布式计算，10000*exp(10000)
#多个进程间传递数据

#线程是分时单核操作，进程是多核操作
import time,threading

def loop():
    print('thread %s is running...'%threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('thread %s >>>%s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended'%threading.current_thread().name)
print('thread %s is running...'%threading.current_thread().name)
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended'%threading.current_thread().name)
#线程上面的变量由所有线程共享。
#进程是各自有一个值

