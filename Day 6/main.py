def find_visit_by_guard_positions(size_width, size_height, objects: list[tuple], guard: list[float, float]):
    direction = 0  # Up, right, down, left
    memo_pos = []

    while True:
        if guard[:] not in memo_pos:
            memo_pos.append(guard[:])
        
        match direction:
            case 0:
                if guard[1] == 0:
                    break
                elif (guard[0], guard[1]-1) in objects:
                    direction = (direction + 1) % 4
                else:
                    guard[1] -= 1
            case 1:
                if guard[0] == size_width-1:
                    break
                elif (guard[0]+1, guard[1]) in objects:
                    direction = (direction + 1) % 4
                else:
                    guard[0] += 1
            case 2:
                if guard[1] == size_height-1:
                    break
                elif (guard[0], guard[1]+1) in objects:
                    direction = (direction + 1) % 4
                else:
                    guard[1] += 1
            case 3:
                if guard[0] == 0:
                    break
                elif (guard[0]-1, guard[1]) in objects:
                    direction = (direction + 1) % 4
                else:
                    guard[0] -= 1

    return len(memo_pos)


if __name__ == '__main__':
    objects = []
    guard = None
    size_width = 0
    size_height = 0
    with open('input.txt', 'r') as file:
        for i, line in enumerate(file):
            for j in range(len(line)):
                if line[j] == "#":
                    objects.append((j, i))
                if line[j] == "^":
                    guard = [j, i]

        size_width = j+1
        size_height = i+1
    
    import time
    s = time.time()
    print(find_visit_by_guard_positions(size_width, size_height, objects, guard))
    print(time.time()-s)