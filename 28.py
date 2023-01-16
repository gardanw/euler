def main(n, start=1):
    spiral = [start]
    step = 2
    while spiral[-1] != n * n:
        control = 0
        for i in range(spiral[-1], n * n + 1, step):
            if i in spiral:
                continue
            else:
                spiral.append(i)
                control += 1
            if control == 4:
                break
        step += 2

    return sum(spiral)


if __name__ == "__main__":
    print(main(1001))
