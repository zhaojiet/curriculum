from  multiprocessing import Process,Queue
import os,time,random

def write(q):
    print('Process to write:%s'%os.getpid())
    for value in ['a','b','c']:
        print('put %s in'%value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read:%s' % os.getpid())
    while True:
        value=q.get(True)
        print('get %s from queue'%value)

if __name__=='__main__':
    print('process：%s'%os.getpid())
    q=Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
