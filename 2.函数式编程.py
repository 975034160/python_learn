#函数式编程   函数也可以作为参数赋值给变量 即变量可以指向函数

ab=abs  #赋值时候 函数不带括号，带括号表示调用，不带括号表示引用
        #本质上来说函数名也是变量
print(ab(-100))


#函数可以赋值给变量  n那么函数也就能作为变量传递给其他函数

# 比如  定义一个计算的函数和四个加减乘除的方法

def jia(a,b):
    return a+b

def jian(a,b):
    return a-b

def chen(a,b):
    return a*b

def chu(a,b):
    return a/b

#计算函数接收两个数字和一个方法
def calculate(a,b,method):
    result= method(a,b)  #使用传入的参数作为计算方法
    print(result)

calculate(4,3,chu)
