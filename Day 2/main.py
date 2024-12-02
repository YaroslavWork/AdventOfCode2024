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

def check_if_code_is_safe_without_level(code: list[int]) -> bool:
    if check_if_code_is_safe(code):
        return True
    
    for i in range(len(code)):
        code_without_level = code[:i] + code[i+1:]
        if check_if_code_is_safe(code_without_level):
            return True
    return False

if __name__ == "__main__":
    codes: list[list[int]] = []

    with open("input.txt", "r") as data:
        for line in data:
            code_str = line.split(" ")
            codes.append(list(map(int, code_str)))

    count_save_codes = 0
    for code in codes:
        count_save_codes += check_if_code_is_safe(code)

    print(count_save_codes)

    #Second part
    count_save_codes_by_removing_a_digit = 0
    for code in codes:
        count_save_codes_by_removing_a_digit += check_if_code_is_safe_without_level(code)

    print(count_save_codes_by_removing_a_digit)