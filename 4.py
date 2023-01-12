def main():
    palindromes = []
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            n = str(i * j)
            if n == n[::-1]:
                palindromes.append(int(n))
    return max(palindromes)


if __name__ == "__main__":
    print(main())
