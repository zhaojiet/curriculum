class Contact_book(object):                        #通讯录
    def __init__(self):
        self.book={}

    def append(self,name,number):
        if name in self.book:
            print('This people existed already')
        else:
            self.book[name]=number
            print('%s is appended successfully'%name)    #检查名字是否存在，在则报错，不在则继续输入号码


    def dele(self,Name):
        if (Name in self.book):
            self.book.pop(Name)
            print('%s is deleted successfully'%Name)
        else:
            print('cannot find this people')       #检查输入名字是否在通讯录中，在则删除，不在则报错

    def search(self,**kw):#根据关键字参数中的key，判断下一步怎么做，不同的key对应不同的操作
        flag=0
        if 'name' in kw:
            if kw['name'] in self.book:
                print('the number is %s'%self.book[kw['name']])#这里的name是字符，前面的name是变量
        elif 'number' in kw:
            for p in self.person:
                if self.book[p]==kw['number']:
                    print('p')
                    print('Number is %s'%kw['number'])
            if flag==0:
                 print('cannot find the people')


    def listall(self):
        for key in self.book:
            print('Name:%s\tTel:%s' % (key, self.book[key])) #循环输出所有的姓名对应的号码




my_book=Contact_book()
while True:
    print('\n1     add_person')
    print('2     modify_person')
    print('3     search_person')
    print('4     del_person')
    print('5     list_person')
    a=input('Please input the choice')
    if a=='1':#键盘键入的input是符号，如果不加引号就是整形值
        name=input('please input name:')
        number=input('please input number:')
        my_book.append(name,number)
    elif a=='3':
        key=input('please input argument:')
        value=input('please input value:')
        if key=='name':
            my_book.search(name=value)
            my_book.search('name'=value)

    elif a=='5':
        my_book.listall()