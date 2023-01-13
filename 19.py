cal = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


def main(year):
    wday = 1
    sunday = 0
    for y in range(1900, year + 1):
        for m in range(1, 13):
            if wday == 0:
                sunday += 1
            if m == 2:
                if (y % 100 != 0 and y % 4 == 0) or (y % 100 == 0 and y % 400 == 0):
                    print(y, m, wday, "p")
                    wday = (wday + (cal[m] + 1) % 7) % 7
                    continue
            print(y, m, wday)
            wday = (wday + cal[m] % 7) % 7
    return sunday


if __name__ == "__main__":
    print(main(2000) - main(1900))
