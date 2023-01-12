def main(n):
    sum_sqrt = sum([i**2 for i in range(n + 1)])
    sqrt_sum = sum([i for i in range(n + 1)]) ** 2
    return sqrt_sum - sum_sqrt


if __name__ == "__main__":
    print(main(100))
