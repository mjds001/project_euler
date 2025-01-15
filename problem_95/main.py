import math

def find_all_divisors(n)-> list:
    """
    find all divisors for a given number, excluding the number itself
    For example, 28 would return [1, 2, 4, 7, 14]
    """
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # Avoid duplicates for perfect squares
                divisors.append(n // i)
    divisors.remove(n)
    return divisors

limit = 1000000
# start by creating a dictionary with each number and the sum of it's divisors
div_dict = {}
for x in range(2,limit):
    div_sum = sum(find_all_divisors(x))
    if div_sum < limit:
        div_dict[x] = div_sum

#print(div_dict)

longest_chain = []

# now look for amicable chains in this list
for x in range(2,limit):
    if x not in div_dict:
        continue
    flag = 0
    chain = [x]
    while flag == 0:
        next_num = div_dict[chain[-1]]
        chain.append(next_num)
        # check if that completes the chain
        if next_num == x:
            print(f'found chain: {chain}')
            if len(chain) > len(longest_chain):
                longest_chain = chain
            flag = 1
        elif next_num not in div_dict:
            flag = 2
            #print(f'chain {chain} is not amicable')
        elif next_num in chain[:-1]:
            flag = 2
            #print(f'chain {chain} is not amicable')
    if flag == 1:
        for num in chain:
            if num in div_dict:
                del div_dict[num]

print(f'longest chain is {longest_chain}')
print(f'smallest number in longest chain is {min(longest_chain)}')
