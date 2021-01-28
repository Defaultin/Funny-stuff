import functools


# decorator for n-times function composition
def composition(func=None, *, repeat=1):
    if func is None:
        return lambda func: composition(func, repeat=repeat)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        while wrapper.count < repeat:
            result = func(result)
            wrapper.count += 1
        return result
    wrapper.count = 1
    return func if repeat == 1 else wrapper


# function for n-times function composition
compose = lambda func, *args, repeat=1: func(*args) if repeat == 1 else func(compose(func, *args, repeat=repeat-1))


def main():
    def f1(x): 
        return x**2
    
    @composition
    def f2(x):
        return x**2
    
    @composition(repeat=5)
    def f3(x): 
        return x**2
    
    print("3^2 =", compose(f1, 3))
    print("3^2^2^2^2 =", compose(f1, 3, repeat=4))
    print("3^2 =", f2(3))
    print("3^2^2^2^2^2 =", f3(3))

    
if __name__ == '__main__':
    main()