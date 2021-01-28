#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import functools
def once(func):
    functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not wrapper.called:
            wrapper.called = True
            func(*args, **kwargs)
    wrapper.called = False
    return wrapper

@once
def massage():
    print("The function called")
    
def main():
    massage()
    massage()
    
if __name__ == '__main__':
    main()

