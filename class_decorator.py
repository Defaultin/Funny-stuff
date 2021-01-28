#!/usr/bin/env python
# coding: utf-8

# In[2]:


from time import perf_counter as tick


class logger:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        t = tick()
        result = self.func(*args, **kwargs)
        print("The method '{0}' was called {1} time with arguments: {2} and keys: {3} and returned {4} in lead time: {5} seconds".format(
            self.func.__name__, self.count, args, kwargs, result, tick() - t))
        return result


@logger
def foo(a, b, keys=None):
    return a + b


def main():
    foo(1, 2, keys=3)


if __name__ == '__main__':
    main()

