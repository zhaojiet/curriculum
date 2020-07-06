#python没必要用全局变量，数据封zhuang
class Student(object):#继承object，还可以继承其它的类
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print('%s:%s'%(self.__name,self.__score))#private 不可改变数据
zhao=Student('zhao','99')
zhao.print_score()

class Animal(object):
    #没有变量，不用初始化数据？？
    def run(self):
        print('animal is running...')
class Dog(Animal):
    def run(self):
        print('dog is running...')#多态，在父类和子类都有run()方法时，子类优先级高于父类
    def eat(self):
        print('dog is eating....')
class Cat(Animal):
    pass
class Husky(Dog):
    pass

d=Dog()
d.run()
d.eat()

print(type(123)) #检测属于那个类，123属于整形类
print(type(d))
print(abs)

h=Husky()
print(isinstance(h,Dog))

print(dir(Dog))

#类属性，实例属性，实例属性优先级高于类属性


class Stu(object):
    name='Stu'
s=Stu()
print(s.name)#类的属性

s.name='shuai'
print(s.name)#实例属性，，高于类属性

#给实例绑定方法
def set_age(self,age):
    self.age=age
from types import MethodType

s.set_age=MethodType(set_age,s)
s.set_age(25)
print(s.age)
