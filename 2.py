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
        return n
    elif n > 2:
        return fibo(n - 1) + fibo(n - 2)


def main(n):
    n_fib = 1
    val = fibo(n_fib)
    sum_val = 0
    while val < n:
        if val % 2 == 0:
            sum_val += val
        n_fib += 1
        val = fibo(n_fib)
    return sum_val


if __name__ == "__main__":
    print(main(4_000_000))
