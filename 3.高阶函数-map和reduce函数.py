'''
map()函数接收两个参数
    第一个是一个函数名 函数接收一个参数
    第二个是一个Iterator  可遍历的集合
    使用传入的函数对 Iterator的每一个值进行计算  然后返回一个新的Iterator
'''

ls=[1,2,3,4,5,6,7]

def f(x):
    return x*x

it=map(f,ls)

for i in  it:
    print(i)

'''
reduce()函数
reduce函数接收两个参数
    第一个参数是一个函数名称，该函数接收两个参数
    第二个函数是一个Iterator 
    reduce函数对Iterator中的前两个值计算，然后用结果继续和下一个值计算  
        比如传入 sum(m,n)  [1,2,3,4,5,6,7]  先计算sum(1,2)>sum(sum(1,2),3).... 
'''
from  functools import reduce

#先定义一个根据传入的字符串取对应数字的函数   传入'2' 返回 2
def fn(n):
    num_list={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return num_list[n]
#定义一个函数 把两个数字转换成两位数
def fx(m,n):
    return 10*m+n

#先使用map函数 把字符串（字符串本伸就是一个序列集合）转换成一个数字的集合 '765'>[7,6,5]
#然后使用reduce函数 对数字序列进行 转换   完成吧字符串转换成数字的需求

#result=reduce(fx,map(fn,'765'))

#使用lambda表达式完成

result=reduce(lambda x,y:x*10+y,map(fn,'567'))

print(result)










