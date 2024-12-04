def check_word_normally_and_reverse(word: str, check_word: str) -> bool:
    return word == check_word or word[::-1] == check_word

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


if __name__ == '__main__':
    words: list[str] = []
    with open('input.txt', 'r') as file:
        for line in file:
            words.append(line[:-1])  # Cut \n

    print(word_search(words))