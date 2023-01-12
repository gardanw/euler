def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def main(n):
    prime = []
    num = 2
    while len(prime) != n:
        if is_prime(num):
            prime.append(num)
        num += 1
    return prime[-1]


if __name__ == "__main__":
    print(main(10001))
