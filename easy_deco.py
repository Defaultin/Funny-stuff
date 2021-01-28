#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import functools
from time import perf_counter as tick


def easy_decorator(deco):
    @functools.wraps(deco)
    def wrapper(*deco_args, **deco_kwargs):
        def decorator(func):
            result = deco(func, *deco_args, **deco_kwargs)
            functools.update_wrapper(result, func)
            return result
        return decorator
    return wrapper


@easy_decorator
def logger(func, *, logger_enabled=True):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        t = tick()
        result = func(*args, **kwargs)
        print("The method '{0}' was called {1} time with arguments: {2} and keys: {3} and returned {4} in lead time: {5} seconds".format(
            func.__name__, wrapper.count, args, kwargs, result, tick() - t))
        return result
    wrapper.count = 0
    return wrapper if logger_enabled else func


@logger(logger_enabled=True)
def foo(a, b, keys=None):
    return a + b

def main():
    foo(2, 3, keys=5)

if __name__ == '__main__':
    main()