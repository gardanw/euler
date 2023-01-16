# -*- coding: utf-8 -*-
def cache_fibo(func):
    cache = {}

    def cache_number(*args, **kwargs):
        if args in cache:
            return cache[args]
        else:
            val = func(*args, **kwargs)
            cache[args] = val
            return val

    return cache_number


@cache_fibo
def fibo(n):
    if n <= 2:
        return 1
    elif n > 2:
        return fibo(n - 1) + fibo(n - 2)


def main(len_d):
    n = 1
    while len(str(fibo(n))) < len_d:
        n += 1
    return n


if __name__ == "__main__":
    print(main(1000))
