#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import functools


def timethis(func=None, *, iter_amount=100):
    if func is None:
        return lambda func: timethis(func, iter_amount=iter_amount)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        lead_time = float("inf")
        for i in range(iter_amount):
            tick = time.perf_counter()
            result = func(*args, **kwargs)
            lead_time = min(lead_time, time.perf_counter() - tick)
        print("Function '{0}' worked {1} iterations in at minimum {2} seconds".format(
            func.__name__, iter_amount, lead_time))
        return result
    return wrapper


@timethis
def foo(a):
    res = 0
    for i in a:
        res += i
    return res


def main():
    f = foo(range(10**5))
    print(f)
    f = timethis(sum)(range(10**5))
    print(f)


if __name__ == '__main__':
    main()

