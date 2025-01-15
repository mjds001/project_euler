from math import gcd, isqrt
import time

"""
Attempt a solution using pythagorean triples.
Solution can be found by joining 2 pythagorean triangles together
Then check if this solution is "almost equalateral"
Look for primitives, and then check if the hypotenuse is with +/- 1 of 2* the base
"""
def coprime(a, b):
    return gcd(a, b) == 1

start_time = time.time()
print('starting...')
perimLim = 1000000000
perim = 0
xLim = (perimLim + 1)/3
x = 3

# generate a list of primitive triples:
c = 0
m = 2
n = 1
k = 1
flag = 0

while flag == 0:
    if m%2==0 or n%2==0: # m and n are not both odd
        if coprime(m,n): # m and n are coprime
            a = (m**2-n**2)
            b = 2*m*n
            c = (m**2 + n**2)
            #print(f'found primitive: {a}, {b}, {c}')
            #print(f'm = {m}, n = {n}')
            # this is a primitive triple, let's check if it fits our solution criteria
            short_side = min(a,b)
            long_side = max(a,b)
            dif = (2*short_side) - c
            #print(f'dif = {dif}')
            if dif == 1 or dif == -1:
                print(f'solution found in primitive triple: {a}, {b}, {c}')
                print(f'solution triangle has sides: {2*short_side}, {c}, {c}')
                #A = short_side * long_side
                #print(f'solution area is {A}')
                perim += (2*short_side + c + c)
    n += 1
    if n == m:
        #print('iterating m')
        n = 1
        m += 1
        if (m**2 + n**2) > xLim:
            flag = 1

print(f'final perim is {perim}')
end_time = time.time()
duration = end_time - start_time
print(f'duration = {duration}')

"""success!!!
final answer: 518408346
"""


