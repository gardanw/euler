alphabet = {chr(65 + i): i + 1 for i in range(26)}


def main(names):
    return sum(
        [(i + 1) * sum([alphabet[l] for l in list(n)]) for i, n in enumerate(names)]
    )


if __name__ == "__main__":
    with open("p022_names.txt", "r") as file:
        line = file.readline()
        names = list(map(lambda x: x.strip('"'), line.split(",")))
        names.sort()
    print(main(names))
