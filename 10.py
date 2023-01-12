def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def main(n):
    primes = []
    for i in range(n):
        if is_prime(i):
            primes.append(i)
    return sum(primes)


if __name__ == "__main__":
    print(main(2_000_000))
