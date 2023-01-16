def main(a_start, a_end, b_start, b_end):
    seq = set()
    for a in range(a_start, a_end + 1):
        for b in range(b_start, b_end + 1):
            seq.add(a**b)
    return len(seq)


if __name__ == "__main__":
    print(main(2, 100, 2, 100))
