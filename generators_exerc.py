# -*- coding: utf-8 -*-
import time


def fibo_gen(max_num=None):
    a, b = 0, 1
    while True:
        yield a
        if b>max_num:
            return
        a, b = b, a+b


if __name__ == '__main__':
    fibonacci = fibo_gen(55)
    for element in fibonacci:
        print(element)
        time.sleep(.35)