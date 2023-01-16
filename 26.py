def main(d):
    num = longest = 1
    for n in range(3, d, 2):
        if n % 5 == 0:
            continue
        p = 1
        while (10**p) % n != 1:
            p += 1
        if p > longest:
            num, longest = n, p
    return num


if __name__ == "__main__":
    print(main(1000))
