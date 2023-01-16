def div(number):
    divisors = set()
    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divisors.add(i)
    for d in list(divisors):
        divisors.add(int(number / d))
    return divisors


def main(n):
    abundant = [i for i in range(1, n + 1) if sum(div(i)) - i > i]
    sum_two_abundant = set()
    for i, a1 in enumerate(abundant):
        for a2 in abundant[i:]:
            sum_two_abundant.add(a1 + a2)
    out = sum([i for i in range(1, n + 1) if i not in sum_two_abundant])
    return out


if __name__ == "__main__":
    print(main(28124))
