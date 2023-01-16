def main():
    numbers = []
    for i in range(2, 200000):
        x = str(i)
        dig_sum = 0
        for cyfra in x:
            dig_sum += int(cyfra) ** 5
        if dig_sum == i:
            numbers.append(i)
    return sum(numbers)


if __name__ == "__main__":
    print(main())
