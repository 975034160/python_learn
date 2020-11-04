#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = '李朋朋'

import sys

def test():
    for i in sys.argv:
        print(i)

'''
当我们在命令行使用脚本时，python解释器会吧__name__替换为“__main__”
而在其他地方导入时候，if条件就会判断失败，不做任何调用。
这个方便在命令行测试，而不影响其他环境导入。
'''
if __name__=="__main__":
    test()


'''
作用域
正常的函数或者变量的作用域都是public
要控制函数或者变量的作用域使用 _

__xxx__表示特殊意义的变量   

_xx
__xx表示私有变量，不应该被引用


'''
