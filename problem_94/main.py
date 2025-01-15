# %%

import math
import time
from math import gcd, isqrt


def coprime(a, b):
    return gcd(a, b) == 1

def is_square(n):
    sqrt = isqrt(int(n))
    return sqrt*sqrt == n

print('starting')
start_time = time.time()


perimLim = 1000000000
xLim = (perimLim + 1)/3
x = 3
perimSum = 0
hSquaredLim = xLim**2 - ((xLim-1)/2)**2
hLim = int(hSquaredLim**0.5 +2)

"""
A = 1/2 * b * h
For A to be an integer, b and h must be integers and one of them must be even
For an iscoceles triange with sides a, a, and b, the height is sqrt(a^2 - (b/2)^2)
For this height to be an integer, a^2 - (b/2)^2 must be a perfect square.
When b = a+1, a^2 - (b/2)^2 = a^2 - ((a+1)/2)^2 = a^2 - (a^2 + 2a + 1)/4 = (3a^2 - 2a - 1)/4
When b = a-1, a^2 - (b/2)^2 = a^2 - ((a-1)/2)^2 = a^2 - (a^2 - 2a + 1)/4 = (3a^2 + 2a - 1)/4
If we factor these, we get (3a+1)(a-1)/4 and (3a-1)(a+1)/4
"""
# %%

# %% 
#xlim is 333333333
solution_areas = []
solution_perims_plus_one = []
solution_perims_minus_one = []
solution_x_plus_one = []
solution_x_minus_one = []
while x <= xLim:
    hSquared = (3*x+1)*(x-1)/4
    if is_square(hSquared):
        h = isqrt(int(hSquared))
        perimSum += 3*x + 1
        Area = (x+1)*h/2
        print(f'solution found in {x} +1. hSquared = {hSquared}, h = {h}. Area = {Area}')
        solution_areas.append(Area)
        solution_perims_plus_one.append(3*x+1)
        solution_x_plus_one.append(x)
    hSquared = (x+1)*(3*x-1)/4
    if is_square(hSquared):
        h = isqrt(int(hSquared))
        perimSum += 3 * x - 1
        Area = (x-1) * h / 2
        print(f'solution found in {x} -1. hSquared = {hSquared}, h = {h}, Area = {Area}')
        solution_areas.append(Area)
        solution_perims_minus_one.append(3*x-1)
        solution_x_minus_one.append(x)
    x += 1


"""
# trying a method using pythagorean triples:

# generate a list of triples (but only include the shortest side and hypotenuse):
triples = {}
c = 0
m = 2
n = 1
k = 1
flag = 0
# each key will be the hypotenuse (x) and each value will be the shortest side in that right triangle
while flag == 0:
    if m%2==0 or n%2==0: # m and n are not both odd
        if coprime(m,n): # m and n are coprime
            a = k*(m**2-n**2)
            b = k*2*m*n
            c = k*(m**2 + n**2)
            triples[c] = min(a,b)
    k += 1
    if k*(m**2 + n**2) > xLim:
        k = 1
        n += 1
        if n == m:
            n = 1
            m += 1
            if k*(m**2 + n**2) > xLim:
                flag = 1

while x < xLim:
    base = (x+1)/2
    if x in triples:
        if triples[x] == base:
            perimSum += 3 * x + 1
            print(f'{x} +1')
    base = (x-1)/2
    if x in triples:
        if triples[x] == base:
            perimSum += 3 * x - 1
            print(f'{x} -1')
    x += 1
"""

# %%

end_time = time.time()
duration = end_time - start_time
print(f'perimSum = {perimSum}')
print(f'duration = {duration}')
print(f'solution_areas = {solution_areas}')
print(f'solution_perims_plus_one = {solution_perims_plus_one}')
print(f'solution_perims_minus_one = {solution_perims_minus_one}')
print(f'solution_x_plus_one = {solution_x_plus_one}')
print(f'solution_x_minus_one = {solution_x_minus_one}')






