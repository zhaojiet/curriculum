#闭包：返回函数会让这些函数同时用一个数值

#匿名函数：不用定义函数名

print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))#把map返回值变为list

print(list(range(0,5)))#
print(range(0,5))

#函数也是一种类型的东西
#这种在代码运行期间动态增加功能的方式，称之为“装饰器”


def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        print(args)
        print(kw)       #引入可变参数和关键字参数让新功能能传入参数
        return  func(*args,**kw)
    return wrapper
@log
def now(*args,**kw):
    print('2015')

now(1,2,c='bei',b='x')


#偏函数，int(x,base=10)
def int(x,base=2):
    return int(x)
print(encode('B'))