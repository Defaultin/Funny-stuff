#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import functools


def delay(func=None, *, enabled=True):
    if func is None:
        return lambda func: delay(func, enabled=enabled)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        if wrapper.count == 1:
            wrapper.storage = None
        wrapper.storage, result = func(*args, **kwargs), wrapper.storage
        return result
    wrapper.count = 0
    return wrapper if enabled else func


@delay(enabled=True)
def foo(x):
    return x


def main():
    for i in range(5):
        print(foo(i))


if __name__ == "__main__":
    main()

