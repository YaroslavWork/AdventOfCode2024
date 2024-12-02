def check_if_code_is_safe(code: list[int]) -> bool:
    if len(code) < 2:
        raise IndexError("Length of code must be more or equal 2")
    is_increasing = True if code[0] < code[1] else False
    for i in range(len(code)-1):
        diff = code[i] - code[i+1]
        if 1 < abs(diff) > 3:
            return False
        if diff <= 0 and not is_increasing or diff >= 0 and is_increasing:
            return False
        
    return True


if __name__ == "__main__":
    codes: list[list[int]] = []
    data: list[str] = open("input.txt", "r")

    for line in data:
        code_str = line.split(" ")
        codes.append(list(map(int, code_str)))

    count_save_codes = 0
    for code in codes:
        count_save_codes += check_if_code_is_safe(code)

    print(count_save_codes)