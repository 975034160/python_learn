# l = [1,2,3,4,5,6,7,8]
# for i in l:
#     print(i)
#
# #列表生产器
#
# ls=[x*x for  x in range(10)]
#
# for i in ls:
#     print(i)
#
# #生成器
#
# g=(x*x for x in range(10))
#
# for i in g:
#     print(i)
#
#
#
def fib(max_value):
    n,a,b=0,0,1
    while n<max_value:
        yield b
        a,b=b,a+b
        n=n+1
    return 'finsh'


for i in fib(5):
    print(i)


