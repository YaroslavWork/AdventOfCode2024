def can_made_this_euqation(equation: list[int], answer: int) -> bool:

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
    for i in range(len(answers)):
        if can_made_this_euqation(equations[i], answers[i]):
            sum += answers[i]

    print(sum)