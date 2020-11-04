'''
内建函数filter()
filter 过滤器  接收两个参数
    第一个参数为函数名
    第二个参数是Iterator
    作用：使用传入函数的规则判断是否保留Iterator中的元素

'''

#判断传入的参数能否被2整除
def fx(m):
    return m%2==0

# result=filter(fx,[1,2,3,4,5,6,7,8])

#使用lambda表达式实现
result=filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8])

#输出的结果中只有2,4,6,8 不能被2整除的元素都被过滤了
for i in result:
    print(i)



