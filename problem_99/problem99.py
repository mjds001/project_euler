import math



def run():
    # open the txt file
    with open('0099_base_exp.txt') as f:
        lines = f.readlines()
        lines = [line.strip().split(',') for line in lines]
        lines = [[int(line[0]), int(line[1])] for line in lines]
    print(lines[0:10])
    # use logs to compare the number of digits in each large number
    most_digits = 0
    largest_base = 0
    largest_exp = 0
    answer = 0
    line_num = 0
    for line in lines:
        line_num += 1
        base, exp = line
        num_digits = math.floor(exp * math.log10(base)) + 1
        if num_digits > most_digits:
            most_digits = num_digits
            largest_base = base
            largest_exp = exp
            answer = line_num
        elif num_digits == most_digits:
            print(f'equal number of digits: {num_digits} on line {line_num}')
            if base > largest_base:
                largest_base = base
                largest_exp = exp
                answer = line_num
            elif base == largest_base:
                if exp > largest_exp:
                    largest_exp = exp
                    answer = line_num
    print(f'most digits: {most_digits}')
    print(f'largest base: {largest_base}')
    print(f'largest exp: {largest_exp}')
    print(f'answer: {answer}')






if __name__ == '__main__':
    run()