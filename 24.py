from itertools import permutations


def main(digits, n):
    per = permutations(digits)
    per = list(per)
    return "".join(list(per[n - 1]))


if __name__ == "__main__":
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    n = 1_000_000
    print(main(digits, n))
