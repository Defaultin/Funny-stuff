#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import functools
def cached_it(func):
    @functools.wraps(func)
    def wrapper(*args, cache={}): 
        if args not in cache:
            cache[args] = func(*args)
            print("write to cache", cache)
        else:
            print("read from cache", cache)
        return cache[args]
    return wrapper

@cached_it
def foo(a, b, c):
    return a**b**c


def main():
    print(foo(1, 2, 3))
    print(foo(1, 3, 2))
    print(foo(2, 1, 3))
    print(foo(2, 3, 1))
    print(foo(3, 2, 1))
    print(foo(3, 1, 2))

    print(foo(2, 3, 1))


if __name__ == "__main__":
    main()

