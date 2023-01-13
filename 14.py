def next_in_seq(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def gen_seq(start):
    seq = [start]
    while seq[-1] != 1:
        seq.append(next_in_seq(seq[-1]))
    return seq


def main(n):
    longest = 1
    start_n = 0
    for i in range(n, 1, -1):
        new_seq = gen_seq(i)
        if len(new_seq) >= longest:
            longest = len(new_seq)
            start_n = i
    return start_n


if __name__ == "__main__":
    n = 10**6
    print(main(n))
