'''
返回函数
高阶函数可以返回一个值，也可以返回一个函数。
'''

def fx(*args):
    def sum():
        s=0
        for i in args:
            s=s+i
        return s
    return sum


ss=fx(1,2,3,4,5)

print(ss())

