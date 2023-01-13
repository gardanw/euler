from math import factorial


def main(n):
    return factorial(2 * n) / (factorial(n) * factorial(n))


if __name__ == "__main__":
    print(main(20))
