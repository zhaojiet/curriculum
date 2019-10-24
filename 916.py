#可变参数，用list和tuple传参,可以传入任意个参数
def calcu(*numbers):
    sum=0;
    for n in numbers:
        sum=sum+n*n
    return sum
print(calcu(0,1,3))

#关键字参数还多了名字，与可变参数比
def person(name,age,**kw):
    print('name',name,'age',age,'others:',kw)
person('zhao',12,city=5)




#命名关键字参数以dic传递，要有key值
L=range(100)
for i in L[::5]:
    print(i)#间隔取值，要考




#python中字典也可迭代
#用collections库中的iterable判断是否可迭代


f=calcu
print(f(1,2,3))
#函数也可以赋值，函数名也是变量

#f=10,则f不再是函数，是一个10的变量
f=abs
def add(x,y,f):
    return f(x)+f(y)
print(add(1,3,f))#函数传参




s=[-1,-2]

for n in map(abs,s):
    print(n)   #map函数返回列表

#reduce()函数