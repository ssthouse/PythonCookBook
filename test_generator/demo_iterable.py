# coding=utf-8
import random


class demo_iterable(object):
    # 实现__next__方法, 使其可以被 next() 内建方法调用
    def __next__(self):
        return self.next()

    def next(self):
        value = random.randint(0, 10)
        if value < 5:
            raise StopIteration
        else:
            return value

    # 创建自身 并返回
    def __iter__(self):
        return demo_iterable()
