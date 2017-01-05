# coding=utf-8
import random


class demo_iterable(object):
    # 1. 实现__next__方法, 使其可以被 next() 内建方法调用
    # 2. 通过实现这个方法, 可以处理未知的事件, 并且可以在迭代过程中随时停止迭代, 比直接 for in 列表要灵活的多
    def __next__(self):
        return self.next()

    def next(self):
        value = random.randint(0, 10)
        if value < 5:
            raise StopIteration
        else:
            return value

    # 实现迭代器接口, 使其可被 for in 调用
    # 创建自身 并返回
    def __iter__(self):
        print("hahaha")
        return demo_iterable()


# 测试在 demo_iterable 自定义的 iterable 类
def test_self_def_iterable():
    iterable = demo_iterable()
    for value in iterable:
        print(value)
test_self_def_iterable()
