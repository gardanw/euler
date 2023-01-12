def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def main(n):
    if is_prime(n):
        return n
    list_prime = []
    for i in range(2, int(n / 2) + 1):
        if is_prime(i) and n % i == 0:
            list_prime.append(i)
        check = 1
        for p in list_prime:
            check *= p
        if check == n:
            break
    return list_prime[-1]


if __name__ == "__main__":
    print(main(600851475143))
