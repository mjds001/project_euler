
"""
problem 98- anagramic squares
answer: BOARD and BROAD are anagramic squares (17689, 18769)

code could be improved- finds all the anagramic squares, but also includes anagramic squares with different letters having the same digital value as other letters (which the probmes says to ignore)
Since there are only a handful of these outliers, the result can be manually checked to find the anagramic squares that meet the problem's criteria
"""

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
    #anagramatic_squares = get_anagramic_squares(squares)
    # find the anagrams that are squares
    largest_square = 0
    num_an_squares = 0
    for word, other_word in anagrams.items():
        if len(word) < 3:
            continue
        check, square, other_square = is_anagramic_square(word, other_word, squares[len(word)])
        if check:
            num_an_squares += 1
            if square > largest_square:
                largest_square = square
            if other_square > largest_square:
                largest_square = other_square
    print(f'largest square: {largest_square}')
    print(f'num anagramic squares: {num_an_squares} out of {len(anagrams) -1} anagrams')


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

    # divvy up into squares of n digits
    n_digit_squares = {}
    for square in squares:
        if len(str(square)) not in n_digit_squares.keys():
            n_digit_squares[len(str(square))] = []
            n_digit_squares[len(str(square))].append(square)
        else:
            n_digit_squares[len(str(square))].append(square)

    return n_digit_squares

def get_anagramic_squares(squares):
    # return a dict of squares that are anagrams of each, ex {1296: 9216, etc}
    anagramic_squares = {}
    for n_digit, n_digit_squares in squares.items():
        print(len(n_digit_squares))
        if n_digit > 5:
            continue
        ignore = []
        for square in n_digit_squares:
            for other_square in n_digit_squares:
                if square == other_square:
                    continue
                if square in ignore:
                    continue
                if sorted(str(square)) == sorted(str(other_square)):
                    if square in anagramic_squares.keys():
                        anagramic_squares[square].append(other_square)
                    else:
                        anagramic_squares[square] = []
                        anagramic_squares[square].append(other_square)
                    ignore.append(other_square)
    print(f'anagramic_squares: {anagramic_squares}')
    return anagramic_squares


def is_anagramic_square(word, anagram, squares):
    for square in squares:
        # check if the square contains the same number multiple times
        mytable = str.maketrans(word, str(square))
        other_square = int(anagram.translate(mytable))
        if other_square in squares:
            # check if the square has multiple of the same number
            max_count = 0
            for char in str(square):
                if str(square).count(char) > max_count:
                    max_count = str(square).count(char)
            max_count_word = 0
            for char in word:
                if word.count(char) > max_count_word:
                    max_count_word = word.count(char)
            if max_count != max_count_word:
                continue
                
            print(f'{word} and {anagram} are anagramic squares ({square}, {other_square})')
            return True, square, other_square
    return False, 0, 0
    


if __name__ == '__main__':
    run()