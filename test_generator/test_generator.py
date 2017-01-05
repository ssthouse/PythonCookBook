# coding=utf-8
def generate_three_num():
    for i in range(5):
        print("yield %d" % i)
        yield i


def test_use_generator():
    for i in generate_three_num():
        i += 1


test_use_generator()
