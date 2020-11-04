import time

#装饰器

def log(func):
    def wrapper(*args):
        print("方法装饰器。。。")
        func(*args)
    return wrapper

#使用注释方式注入装饰器 ，当调用echoTime时，调用log函数来完成代理调用。
@log
def echoTime(sss):
    print(sss+str(time.time()))

echoTime("This time is :")
