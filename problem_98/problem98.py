    

def run():
    # open the txt file
    with open('0098_words.txt') as f:
        words = f.read().split(',')
        words = [word[1:-1] for word in words]
    anagrams = get_anagrams(words)
    longest_len = 0
    for anagram in anagrams.keys():
        longest_len = len(anagram) if len(anagram) > longest_len else longest_len
    print(longest_len)

    squares = get_squares_of_n_digits(longest_len)
    print(squares)

def get_anagrams(words: list) -> dict:
    anagrams = {}
    sorted_words = {}
    for word in words:
        sorted_words[word] = sorted(word)
    
    for word, sorted_word in sorted_words.items():
        for other_word, other_sorted_word in sorted_words.items():
            if sorted_word == other_sorted_word:
                if word == other_word:
                    continue
                if other_word in anagrams.keys():
                    continue
                anagrams[word] = other_word
    

    print(f'anagrams: {anagrams}')
    return anagrams

def get_squares_of_n_digits(num_digits):
    squares = [100]
    n = 10
    while len(str(squares[-1])) <= num_digits:
        # check to see if the number has any 
        squares.append(n*n)
        n += 1

    return squares








if __name__ == '__main__':
    run()