def main(t):
    t.reverse()
    for i in range(1, len(t)):
        for j in range(len(t[i])):
            t[i][j] = t[i][j] + max([t[i - 1][j], t[i - 1][j + 1]])
    return t[-1][-1]


if __name__ == "__main__":
    with open("p067_triangle.txt", "r") as file:
        triangle = file.readlines()
    triangle = list(map(lambda x: list(map(int, x.strip("\n").split(" "))), triangle))
    print(main(triangle))
