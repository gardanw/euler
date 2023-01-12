def main(n):
    for a in range(1, n - 2):
        for b in range(a, n - 1):
            for c in range(b, n):
                if a + b + c == n and a**2 + b**2 == c**2:
                    return a * b * c


if __name__ == "__main__":
    print(main(1000))
