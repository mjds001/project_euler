
import math
import time


def run():
    d = 2
    fundamental = find_fundamental_solution(d)
    x_n, y_n = fundamental
    flag = True
    while flag == True:
        x_n, y_n = find_solution((x_n, y_n))
        total = (1 + x_n)/2
        blue = (1 + math.sqrt((2*total**2 - 2*total + 1))) / 2
        if total > 10**12:
            flag = False
            solution = (blue, total)

    end_time = time.time()
    print(f'elapsed time: {end_time - start_time} seconds')
    print(f'solutions: {solution}')


def find_fundamental_solution(d):
    """
    itterate to find the fundamental solution to the negative pell equation 
    x^2 - dy^2 = -1
    """
    x = 1
    while True:
        y = math.sqrt((1/d)*(x**2 +1))
        if y == int(y):
            return (x,y)
        else:
            x += 1

def find_solution(prev_sol):
    """
    find the next solution to the negative pell equation x^2 - 2y^2 = -1
    given the fundamental solution and the previous solution
    """
    xprev, yprev = prev_sol
    xnext = 3*xprev + 4*yprev
    ynext = 2*xprev + 3*yprev
    
    return (round(xnext), round(ynext))

if __name__ == "__main__":
    start_time = time.time()
    run()