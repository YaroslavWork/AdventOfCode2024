def next_possibilities(numbers: list[int], base: int = 2) -> list[int]:
    numbers[-1] += 1
    for i in range(len(numbers)):
        if numbers[-i-1] == base:
            try:
                numbers[-i-2] += 1
                numbers[-i-1] = 0
            except IndexError:
                for j in range(len(numbers)):
                    numbers[j] = 0
                break

    return numbers


def can_made_this_euqation(equation: list[int], answer: int) -> bool:
    if len(equation) == 1:
        return equation[0] == answer

    max_pos = 2 ** (len(equation)-1)
    for i in range(max_pos):
        sum = equation[0]
        for j in range(len(equation)-1):
            is_multiplier = (i >> j) & 1
            if is_multiplier:
                sum *= equation[j+1]
            else:
                sum += equation[j+1]
        
        if sum == answer:
            return True
    
    return False


def can_made_this_euqation2(equation: list[int], answer: int) -> bool:
    max_pos = 3 ** (len(equation)-1)
    pos = [0 for i in range(len(equation)-1)]
    
    for i in range(max_pos):
        sum = equation[0]
        for j in range(len(pos)):
            if pos[j] == 0:
                sum *= equation[j+1]
            elif pos[j] == 1:
                sum += equation[j+1]
            else:
                sum = int(str(sum)+str(equation[j+1]))
        
        if sum == answer:
            return True

        pos = next_possibilities(pos, base=3)

    return False


if __name__ == "__main__":
    equations: list[list[int]] = []
    answers: list[int] = []
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.split('\n')[0]
            split_by_semicolons = line.split(':')
            answers.append(int(split_by_semicolons[0]))
            equations.append(split_by_semicolons[1][1:].split(' '))
            equations[-1] = list(map(int, equations[-1]))

    sum = 0
    sum2 = 0
    for i in range(len(answers)):
        if can_made_this_euqation(equations[i], answers[i]):
            sum += answers[i]
        elif can_made_this_euqation2(equations[i], answers[i]):
            sum2 += answers[i]
    print(sum)
    print(sum+sum2)