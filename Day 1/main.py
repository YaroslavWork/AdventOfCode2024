def get_distance(first_column: list[int], second_column: list[int]) -> int:
    first_column.sort()
    second_column.sort()

    sum = 0
    for i in range(len(first_column)):
        sum += abs(first_column[i] - second_column[i])

    return sum


def get_distance2(first_column: list[int], second_column: list[int]) -> int:
    second_column.sort()
    repeated = {}

    number = second_column[0]
    count = 0
    for i in range(len(second_column)):
        if second_column[i] == number:
            count += 1
        else:
            repeated[number] = count
            number = second_column[i]
            count = 1

    sum = 0
    for i in range(len(first_column)):
        number = first_column[i]
        counts = repeated.get(number, 0)
        sum += number*counts

    return sum


if __name__ == "__main__":
    first_column: list[int] = []
    second_column: list[int] = []
    with open("input.txt", "r") as data:
        # Transform data
        for line in data:
            numbers = line.split("   ")
            first_column.append(int(numbers[0]))
            second_column.append(int(numbers[1][:-1]))
    
    print(get_distance(first_column, second_column))
    print(get_distance2(first_column, second_column))