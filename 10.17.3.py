import time,threading
balance=0
lock=threading.Lock()

def change_it(n):
    global balance
    balance=balance+n
    balance=balance-n

def run_thread(n):

    for i in range(10000000):

        try:lock.acquire()
            change_it(n)
        finally:
            lock.release()
t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

#浏览器端口号都是80，怎么区分不同浏览器