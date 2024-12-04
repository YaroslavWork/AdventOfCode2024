def check_word_normally_and_reverse(word: str, check_word: str) -> bool:
    return word == check_word or word[::-1] == check_word

def check_if_it_is_mas(letter1, letter2) -> bool:
    return letter1 == "M" and letter2 == "S" or letter1 == "S" and letter2 == "M"

def word_search(words: list[str]) -> int:
    SEARCH_WORD = "XMAS"
    count = 0
    
    # Horizontal search
    for i in range(len(words)):
        for j in range(len(words[i])-len(SEARCH_WORD)+1):
            expression = words[i][j:j+len(SEARCH_WORD)]
            if check_word_normally_and_reverse(expression, SEARCH_WORD):
                count += 1

    # Vertical search
    for i in range(len(words)-len(SEARCH_WORD)+1):
        for j in range(len(words[i])):
            expression = "".join([words[i+k][j] for k in range(0, len(SEARCH_WORD))])
            if check_word_normally_and_reverse(expression, SEARCH_WORD):
                count += 1

    # Diagonal from left to right search
    for i in range(len(words)-len(SEARCH_WORD)+1):
        for j in range(len(words)-len(SEARCH_WORD)+1):
            expression = "".join([words[i+k][j+k] for k in range(0, len(SEARCH_WORD))])
            if check_word_normally_and_reverse(expression, SEARCH_WORD):
                count += 1
    
    # Diagonal from right to left search
    for i in range(len(words)-len(SEARCH_WORD)+1):
        for j in range(len(SEARCH_WORD)-1, len(words)):
            expression = "".join([words[i+k][j-k] for k in range(0, len(SEARCH_WORD))])
            if check_word_normally_and_reverse(expression, SEARCH_WORD):
                count += 1

    return count


def find_x_mas(words: list[str]) -> int:
    count = 0

    for i in range(1, len(words)-1):
        for j in range(1, len(words)-1):
            
            if words[i][j] == "A" and check_if_it_is_mas(words[i-1][j-1], words[i+1][j+1]) and\
                check_if_it_is_mas(words[i+1][j-1], words[i-1][j+1]):
                count += 1

    return count

if __name__ == '__main__':
    words: list[str] = []
    with open('input.txt', 'r') as file:
        for line in file:
            words.append(line[:-1])  # Cut \n

    print(word_search(words))
    print(find_x_mas(words))