import inflect


def main(n):
    p = inflect.engine()
    s = 0
    for i in range(1, n + 1):
        s += len(p.number_to_words(i).replace(" ", "").replace("-", ""))
    return s


if __name__ == "__main__":
    print(main(1000))
