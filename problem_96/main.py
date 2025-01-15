import pandas as pd

def is_solved(puzzle):
    """
    check if a puzzle df is solved
    If solved, return True
    else return false
    """
    for row in range(0,9):
        for col in range(0,9):
            if type(puzzle.iloc[row, col]) == str:
                return False
    return True

def can_be_solved(puzzle):
    """
    check if a puzzle can be solved.
    Check this by looking to see if there are any empty strings in the puzzle []
    """
    for row in range(0,9):
        for col in range(0,9):
            if type(puzzle.iloc[row, col]) == str:
                if eval(puzzle.iloc[row, col]) == []:
                    return False
    return True

def actually_solved(puzzle):
    """
    check if a puzzle is actually solved
    """
    for row in range(0,9):
        row_check = [1,2,3,4,5,6,7,8,9]
        for col in range(0,9):
            if puzzle.iloc[row, col] in row_check:
                row_check.remove(puzzle.iloc[row, col])
            else:
                return False
            
    for col in range(0,9):
        col_check = [1,2,3,4,5,6,7,8,9]
        for row in range(0,9):
            if puzzle.iloc[row, col] in col_check:
                col_check.remove(puzzle.iloc[row, col])
            else:
                return False
            
    for box_row in range(0,3):
        for box_col in range(0,3):
            box_check = [1,2,3,4,5,6,7,8,9]
            for i in range(0,3):
                for j in range(0,3):
                    if puzzle.iloc[box_row*3+i, box_col*3+j] in box_check:
                        box_check.remove(puzzle.iloc[box_row*3+i, box_col*3+j])
                    else:
                        return False

    return True

def first_pass(puzzle):
    # convert the numbers in the puzzle to ints
    puzzle = puzzle.astype(int)
    # start by filling in the squares which we can deduce from the row, column, and box
    changed = True
    while changed == True:
        changed = False
        for row in range(0,9):
            for col in range(0,9):
                if puzzle.iloc[row, col] == 0:
                    possible = [1,2,3,4,5,6,7,8,9]
                    # check row
                    for i in range(0,9):
                        if puzzle.iloc[row, i] != 0:
                            if puzzle.iloc[row, i] in possible:
                                possible.remove(puzzle.iloc[row, i])
                    # check column
                    for j in range(0,9):
                        if puzzle.iloc[j, col] != 0:
                            if puzzle.iloc[j, col] in possible:
                                possible.remove(puzzle.iloc[j, col])
                    # check box
                    box_row = row // 3
                    box_col = col // 3
                    for i in range(0,3):
                        for j in range(0,3):
                            if puzzle.iloc[box_row*3+i, box_col*3+j] != 0:
                                if puzzle.iloc[box_row*3+i, box_col*3+j] in possible:
                                    possible.remove(puzzle.iloc[box_row*3+i, box_col*3+j])
                    # if there is only one possible number, fill it in
                    if len(possible) == 1:
                        puzzle.iloc[row, col] = possible[0]
                        changed = True
                    else:
                        puzzle.iloc[row, col] = str(possible)
    return puzzle


def solve_puzzle(puzzle):
    # now we need to check if there are any numbers which can only go in one place in a row, column, or box
    print('attempting to solve puzzle...')
    changed = True
    while changed == True:
        changed = False
        for row in range(0,9):
            for col in range(0,9):
                if type(puzzle.iloc[row, col]) == str:
                    possibles = eval(puzzle.iloc[row, col])
                    new_possibles = possibles.copy()
                    spot_change = False
                    for possible in possibles:
                        # check row
                        other_option = False
                        for i in range(0,9):
                            if i == col:
                                pass
                            elif type(puzzle.iloc[row, i]) == str:
                                if possible in eval(puzzle.iloc[row, i]):
                                    other_option = True
                            elif possible == puzzle.iloc[row, i]:
                                if possible in new_possibles:
                                    new_possibles.remove(possible)
                                break
                            if i==8 and other_option==False:
                                puzzle.iloc[row, col] = possible
                                spot_change = True
                                changed = True
                        if spot_change == True:
                            break
                        # check column
                        other_option = False
                        for j in range(0,9):
                            if j == row:
                                pass
                            elif type(puzzle.iloc[j, col]) == str:
                                if possible in eval(puzzle.iloc[j, col]):
                                    other_option = True
                            elif possible == puzzle.iloc[j, col]:
                                if possible in new_possibles:
                                    new_possibles.remove(possible)
                                break
                            if j==8 and other_option==False:
                                spot_change = True
                                puzzle.iloc[row, col] = possible
                                changed = True
                        if spot_change == True:
                            break
                        # check box
                        box_row = row // 3
                        box_col = col // 3
                        stop_flag = False
                        other_option = False
                        for i in range(0,3):
                            for j in range(0,3):
                                if box_row*3 + i == row and j+ box_col*3 == col:
                                    pass
                                elif type(puzzle.iloc[box_row*3+i, box_col*3+j]) == str:
                                    if possible in eval(puzzle.iloc[box_row*3+i, box_col*3+j]):
                                        other_option = True
                                elif possible == puzzle.iloc[box_row*3+i, box_col*3+j]:
                                    if possible in new_possibles:
                                        new_possibles.remove(possible)
                                    stop_flag = True
                                    break
                                if i==2 and j==2 and other_option==False:
                                    puzzle.iloc[row, col] = possible
                                    changed = True
                            if stop_flag == True:
                                break
                    if spot_change == False:
                        if len(new_possibles) == 1:
                            puzzle.iloc[row, col] = new_possibles[0]
                            changed = True
                        elif possibles != new_possibles:
                            puzzle.iloc[row,col] = str(new_possibles)
                            changed = True
    
    if is_solved(puzzle) == True and actually_solved(puzzle) == True:
        status = 'solved'
        print('puzzle solved')
        print(puzzle)
        return status, puzzle
    elif is_solved(puzzle) == True and actually_solved(puzzle) == False:
        status = 'unsolvable'
        print('puzzle unsolvable')
        return status, puzzle
    elif can_be_solved(puzzle) == False:
        status = 'unsolvable'
        print('puzzle unsolvable')
        return status, puzzle
    else:
        status = 'not solved'
        print('puzzle not solved')
        return status, puzzle

def guess_and_check(puzzle):
    # first we will find the square with the least number of possible options
    print('guessing and checking')
    min_options = 9
    for row in range(0,9):
        for col in range(0,9):
            if type(puzzle.iloc[row, col]) == str:
                if len(eval(puzzle.iloc[row, col])) < min_options:
                    min_options = len(eval(puzzle.iloc[row, col]))
                    min_row = row
                    min_col = col
    options = eval(puzzle.iloc[min_row, min_col])
    og_puzzle = puzzle.copy()
    # try each option
    for option in options:
        puzzle = og_puzzle.copy()
        puzzle.iloc[min_row, min_col] = option
        print(f'guessing {option} from {options} at {min_row}, {min_col}')
        # now try to solve this puzzle
        status, new_puzzle = solve_puzzle(puzzle)
        if status == 'solved':
            return status, new_puzzle
        elif status == 'not solved':
            status, new_puzzle = guess_and_check(new_puzzle)
            if status == 'solved':
                return status, new_puzzle
        elif status == 'unsolvable':
            # continue to the next option
            pass

    return status, new_puzzle



# import sudoku.txt as a dataframe
df = pd.read_csv('sudoku.txt', sep=' ', header=None)
# separate each digit of the soduku into its own column in the df
df = df[0].apply(lambda x: pd.Series(list(x)))
final_answer = 0
for grid in range(1,51):
    print('--------------------------------------')
    puzzle = df.iloc[(grid-1)*10+1:grid*10, 0:9]
    print(f'solving grid: {grid}')
    puzzle = df.iloc[(grid-1)*10+1:grid*10, 0:9]
    puzzle = first_pass(puzzle)
    status, new_puzzle = solve_puzzle(puzzle)
    if status == 'solved':
        print('puzzle solved')
    elif status == 'not solved':
        print('puzzle not solved')
        status, new_puzzle = guess_and_check(new_puzzle)

    # check if the solution is actually correct
    if is_solved(new_puzzle) == False:
        print('solution is incorrect')
        break
    else:
        print('solution is correct')
    # get the top left 3 digits of the solved puzzle and combine them to form a 3 digit number
    top_3_digits = new_puzzle.iloc[0,0:3]
    top_3_digits = top_3_digits.apply(lambda x: str(x))
    top_3_digits = ''.join(top_3_digits)
    print(f'top 3 digits: {top_3_digits}')
    # add this to the final answer
    final_answer += int(top_3_digits)
print(f'final answer: {final_answer}')
    


