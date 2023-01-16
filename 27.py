def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def main(a_range, b_range):
    best_a = 1
    best_b = 1
    best_prime_count = 0

    for a in range(-a_range + 1, a_range):
        for b in range(-b_range, b_range + 1):
            n = 0
            prime_count = 0
            while is_prime((n**2) + (a * n) + b):
                prime_count += 1
                n += 1
            if prime_count > best_prime_count:
                best_a = a
                best_b = b
                best_prime_count = prime_count
    return best_a * best_b


if __name__ == "__main__":
    print(main(1000, 1000))
