def main(n):
    return sum(map(int, list(str(n))))


if __name__ == "__main__":
    n = 2**1000
    print(main(n))
