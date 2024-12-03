def find_a_mul_sequence_and_return_sum(sequence):
    # Split by 'mul('
    start_with_prefix = sequence.split("mul(")

    # If sequence do not start from 'mul(' delete first split
    if sequence[0:4] != "mul(":
        del start_with_prefix[0]

    # Find a close bracket ')' in every starting sequence
    sum = 0
    for i in range(len(start_with_prefix)):
        bracket_split = start_with_prefix[i].split(')')[0]
        
        divide_by_comma = bracket_split.split(',')

        if len(divide_by_comma) == 2 and 1 <= len(divide_by_comma[0]) <= 3 and 1 <= len(divide_by_comma[1]) <= 3 and\
            divide_by_comma[0].isdigit() and divide_by_comma[1].isdigit():
            sum += int(divide_by_comma[0])*int(divide_by_comma[1])

    return sum


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        sequence = file.read()
    
    print(find_a_mul_sequence_and_return_sum(sequence))