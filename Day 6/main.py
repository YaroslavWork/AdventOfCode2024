def next_move(size_width: int, size_height: int, objects: list[tuple], guard: list[int, int], direction) -> [int, int, int]:
    match direction:
        case 0:
            if guard[1] == 0:
                return None
            elif (guard[0], guard[1]-1) in objects:
                return [guard[0], guard[1], (direction + 1) % 4]
            else:
                return [guard[0], guard[1]-1, direction]
        case 1:
            if guard[0] == size_width-1:
                return None
            elif (guard[0]+1, guard[1]) in objects:
                return [guard[0], guard[1], (direction + 1) % 4]
            else:
                return [guard[0]+1, guard[1], direction]
        case 2:
            if guard[1] == size_height-1:
                return None
            elif (guard[0], guard[1]+1) in objects:
                return [guard[0], guard[1], (direction + 1) % 4]
            else:
                return [guard[0], guard[1]+1, direction]
        case 3:
            if guard[0] == 0:
                return None
            elif (guard[0]-1, guard[1]) in objects:
                return [guard[0], guard[1], (direction + 1) % 4]
            else:
                return [guard[0]-1, guard[1], direction]


def find_visit_by_guard_positions(size_width: int, size_height: int, objects: list[tuple], guard: list[int, int]) -> int:
    direction = 0  # Up, right, down, left
    memo_pos = []

    next_pos_with_dir = [guard[0], guard[1], direction]
    while next_pos_with_dir != None:
        if next_pos_with_dir[0:2] not in memo_pos: # without direction
            memo_pos.append(next_pos_with_dir[0:2])
        
        next_pos_with_dir = next_move(size_width, size_height, objects, next_pos_with_dir[0:2], next_pos_with_dir[2])

    return len(memo_pos)


def find_loops(size_width: int, size_height: int, objects: list[tuple], guard: list[int, int]) -> int:
    main_direction = 0
    main_pos = [guard[0], guard[1]]
    objects_making_loops_pos = []
    
    while True:
        memo_pos_with_dir = []
        sim_pos = [main_pos[0], main_pos[1]]
        sim_direction = main_direction
        main_step = next_move(size_width, size_height, objects, main_pos, main_direction)
        if main_step is None:
            return len(set(objects_making_loops_pos))
        main_pos = [main_step[0], main_step[1]]
        main_direction = main_step[2]
        objects_with_new_one = objects + [(main_step[0], main_step[1])]
        while True:
            if [sim_pos[0], sim_pos[1], sim_direction] in memo_pos_with_dir:
                objects_making_loops_pos.append((main_step[0], main_step[1]))
                break
            else:
                memo_pos_with_dir.append([sim_pos[0], sim_pos[1], sim_direction])
            
            step = next_move(size_width, size_height, objects_with_new_one, sim_pos, sim_direction)
            if step is None:
                break
            else:
                sim_pos = [step[0], step[1]]
                sim_direction = step[2]

        


if __name__ == '__main__':
    objects: list[tuple] = []
    guard: list[int, int] = None
    size_width: int = 0
    size_height: int = 0
    with open('input.txt', 'r') as file:
        for i, line in enumerate(file):
            for j in range(len(line)):
                if line[j] == "#":
                    objects.append((j, i))
                if line[j] == "^":
                    guard = [j, i]

        size_width = j+1
        size_height = i+1
    
    print(find_visit_by_guard_positions(size_width, size_height, objects, guard))
    print(find_loops(size_width, size_height, objects, guard))  # 3.5 minutes