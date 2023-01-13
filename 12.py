def div(number):
    divisors = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisors.append(i)
    for d in divisors[:]:
        divisors.append(int(number / d))
    return divisors


def main(div_end):
    n = 1
    ite = 1
    div_len = 1
    while div_len <= div_end:
        div_len = len(div(n))
        ite += 1
        n += ite
    return n - ite


if __name__ == "__main__":
    print(main(500))
