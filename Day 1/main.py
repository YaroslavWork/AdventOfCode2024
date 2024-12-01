def get_distance(first_column: list[int], second_column: list[int]) -> int:
    first_column.sort()
    second_column.sort()

    sum = 0
    for i in range(len(first_column)):
        sum += abs(first_column[i] - second_column[i])
        print(f"abs({first_column[i]} - {second_column[i]}) = {abs(first_column[i]-second_column[i])}")

    return sum

if __name__ == "__main__":
    first_column: list[int] = []
    second_column: list[int] = []
    data: list[str] = open("input.txt", "r")

    # Transform data
    for line in data:
        numbers = line.split("   ")
        first_column.append(int(numbers[0]))
        second_column.append(int(numbers[1][:-1]))
    
    print(get_distance(first_column, second_column))