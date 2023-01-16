def div(number):
    divisors = []
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisors.append(i)
    for d in divisors[:]:
        divisors.append(int(number / d))
    return divisors


def main(n):
    pair_set = set()
    for i in range(n, 0, -1):
        if i in pair_set:
            continue
        div_sum1 = sum(div(i)) - i
        if div_sum1 == i:
            continue
        div_sum2 = sum(div(div_sum1)) - div_sum1
        if i == div_sum2:
            pair_set.add(div_sum1)
            pair_set.add(div_sum2)

    return sum(pair_set)


if __name__ == "__main__":
    print(main(10000))
