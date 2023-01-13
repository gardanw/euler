def main(n):
    frac = 1
    for i in range(1, n + 1):
        frac *= i
    return sum(map(int, list(str(frac))))


if __name__ == "__main__":
    print(main(100))
