#10.14

#processing 进程  thread 线程

#fork（）系统调用（os模块有常见的系统调用） 父进程返回子进程ID 子进程返回0

#多核 可以真正实现多进程

#os.getpid() os.getppid()

from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s)...'%(name,os.getpid()))

if __name__=='__main__':
    print('Parent process %s'% os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('Child process till start')
    p.start()
    p.join()
    print('Child process end')
