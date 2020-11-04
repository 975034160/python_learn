'''
sorted()函数可以接收1或2个参数
    第一个参数是序列
    第二个参数是可选的参数 key  key接收的是一个函数名称
    sorted函数对传入的序列进行排序 如果传入了key，则使用key值函数计算后排序，返回的结果是计算前的元素。

'''

nums=[1,3,-5,19,2,6,-7]

it=sorted(nums,key=abs)

for i in it:
    print(i)
