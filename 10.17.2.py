import time,threading
balance=0

def change_it(n):
    global balance
    balance=balance+n
    balance=balance-n

def run_thread(n):
    for i in range(10000):
        change_it(n)
    print(threading.current_thread().name)
t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

#可以看到，结果有时不为零，即线程t1和t2混乱了，将balance的值改错了。