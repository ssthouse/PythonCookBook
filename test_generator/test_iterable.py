# coding=utf-8
# 学习迭代器 & 生成器 的测试代码


# 从下面对于 list 测试来看, 加了 enumerate  iterate 出来的数据多一个 index, 然后是 value
# enumerate 实现了类似于一个枚举的功能, 使可迭代对象多一个 index, 即迭代 enumerate 对象得到的是(index, value)
# 测试 enumerate 内建方法
from test_generator.demo_iterable import demo_iterable


def test_enumerate():
    my_str = 'abc'
    # 其实是创建一个 enumerate对象, 这个对象是可以被迭代的
    for i, _ in enumerate(my_str):
        print(i)
        print(_)


# test_enumerate()


# 测试直接从 list进行迭代的区别
def test_list():
    my_list = [(1, 2), (2, 3), (3, 4)]
    for index, value in my_list:
        print("%d %d" % (index, value))


# test_list()


# 测试 iter 内建方法
def test_iter():
    my_list = [1, 2, 3]
    iterable = iter(my_list)
    while True:
        try:
            print(next(iterable))
        except StopIteration:
            print("stop iteration")
            break


# test_iter()

# 测试在 demo_iterable 自定义的 iterable 类
def test_self_def_iterable():
    iterable = demo_iterable()
    for value in iterable:
        print(value)


test_self_def_iterable()
