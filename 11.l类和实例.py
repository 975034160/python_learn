
'''
面向对象最重要的概念就是类和实例
类是抽象的模板，实例是根据类创建出来的对象。

变量的访问限制
    因为公有变量会被外部代码修改，不安全
    所以使用_xxx变量来隐藏变量 提供getXxx()方法来访问变脸
    python 中私有变量还是可以访问 但是规定不允许访问修改私有变量
    _xxx和__xx变量的区别
    __xxx会被编译器替换成_类名__xxx 但是不同的编译器可能替换的不一样
'''

class Student(object):
    def __init__(self,xh,name,age):
        self._xh=xh
        self._name=name
        self._age=age

    def getXh(self):
        return self._xh

    def getName(self):
        return self._name

    def getAge(self):
        return self._age
    def print_info(self):
        print('学号：%s  姓名：%s  年龄：%s'%(self._xh,self._name,self._age))

# student=Student(1,"lipeng",19)

# print(student.getXh(),student.getName(),student.getAge())
# student.print_info()


class Teacher(object):
    def __init__(self,name,age,clazz):
        self.name = name
        self.age = age
        self.clazz = clazz

    def showInfo(self):
        print('[ 姓名：%s 年龄：%d 课程：%s ]' % (self.name,self.age,self.clazz))


# teacher = Teacher('李朋朋',26,'物理')
# teacher.showInfo()

print(9//2)