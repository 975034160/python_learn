'''
functools的偏函数功能
functools.partial


'''

# from  functools import partial


'''
使用自定义的partial函数来实现 functools的partial函数
*arg表示任意多个无名参数，类型为tuple;**kwargs表示关键字参数，为dict。
'''
def partial(func,**kwargs):
    def wrapper(*args):
        return func(*args,**kwargs)
    return wrapper



#使用functools的partial函数来固定int的参数默认值
int2=partial(int,base=2)

num=int2('1110111')

print(num)
