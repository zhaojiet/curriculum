from functools import reduce
digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return digits[s]
    return reduce(fn,map(char2num,s))        #reduce返回一个值
print(str2int(['9','7','6','5','2']))

#filter()

def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum

f=lazy_sum(1,3,5,7,9)
f1=lazy_sum(1,3,5,7,9)

if (f==f1):
    print('true')
else:
    print('false')
print(f()*2)    #有括号才是运行的函数


for n in range(1,4):
    print(n)               #只能取1，2，3

def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 =count()

print(f1())       #为啥返回9
                  #返回值是函数会出现闭包问题，所有函数引用值一样//考试出
print('a'.encode('utf-8'))

for w in 'daas':
    print(w)