from  multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run task %s(%s)..'%(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()#进程运行的时间
    print('the %s run %0.2f seconds'%(name,(end-start)))

if __name__=='__main__':
    print('parent process %s'%os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task(i))
    print('waiting...')
    p.close()
    p.join()
    print('done')
    
    #嘿嘿
