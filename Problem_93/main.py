from itertools import permutations
from itertools import product


def evaluate(nums, signs):
    outputs = []
    try:
        outputs.append(eval(f'{nums[0]} {signs[0]} {nums[1]} {signs[1]} {nums[2]} {signs[2]} {nums[3]}'))
    except:
        #print(f'{nums[0]} {signs[0]} {nums[1]} {signs[1]} {nums[2]} {signs[2]} {nums[3]}')
        pass
    try:
        outputs.append(eval(f'{nums[0]} {signs[0]} ( {nums[1]} {signs[1]} {nums[2]}) {signs[2]} {nums[3]}'))
    except:
        #print(f'{nums[0]} {signs[0]} ( {nums[1]} {signs[1]} {nums[2]}) {signs[2]} {nums[3]}')
        pass
    try:
        outputs.append(eval(f'{nums[0]} {signs[0]} ( {nums[1]} {signs[1]} {nums[2]} {signs[2]} {nums[3]})'))
    except:
       # print(f'{nums[0]} {signs[0]} ( {nums[1]} {signs[1]} {nums[2]} {signs[2]} {nums[3]})')
        pass
    try:
        outputs.append(eval(f'{nums[0]} {signs[0]}  {nums[1]} {signs[1]} ({nums[2]}) {signs[2]} {nums[3]}'))
    except:
       # print(f'{nums[0]} {signs[0]}  {nums[1]} {signs[1]} ({nums[2]}) {signs[2]} {nums[3]}')
        pass
    try:
        outputs.append(eval(f'({nums[0]} {signs[0]}  {nums[1]}) {signs[1]} ({nums[2]} {signs[2]} {nums[3]})'))
    except:
       # print(f'({nums[0]} {signs[0]}  {nums[1]}) {signs[1]} ({nums[2]} {signs[2]} {nums[3]})')
        pass
    outputs = [x for x in outputs if x%1==0 and x>0]
    return outputs



numbers = [1,2,3,4,5,6,7,8,9]
count = 0
max_consec = 0
# 3024 total num perms
for nums in list(permutations(numbers,4)):
    print(count)
    count+=1
    num_perms = list(permutations(nums))
    signs = ['*','+','-','/']
    sign_perms = list(product(signs, repeat = 3))
    ints = []

    for nums in num_perms:
        for signs in sign_perms:
            ints = ints + evaluate(nums, signs)

    ints = list(set(ints))

    if ints[0] == 1:
        consec_len = 0
        for x in range(len(ints)):
            if ints[x] + 1 != ints[x+1]:
                if (x+1) > max_consec:
                    max_consec = x+1
                    max_nums = nums
                break


print(max_nums)
print(max_consec)

