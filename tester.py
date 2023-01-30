import random
import numpy as np


def operations(sz):
    ops = []
    for i in range(sz-1):
        ops.append(random.randint(1, 4))
    return ops


def add(v1, v2):
    val = v1 + v2
    return val


def sub(v1, v2):
    val = v1 - v2
    return val


def mult(v1, v2):
    val = v1 * v2
    return val


def div(v1, v2):
    val = v1 / v2
    return val


def algebra(sets, sz):
    ops = operations(sz)
    print(ops)
    if ops != []:
        for i in range(sz - 1):
            if ops[i] == 1:
                ans = add(sets[i], sets[i + 1])
            elif ops[i] == 2:
                ans = sub(sets[i], sets[i + 1])
            elif ops[i] == 3:
                ans = mult(sets[i], sets[i + 1])
            else:
                ans = div(sets[i], sets[i + 1])
            sets[i + 1] = ans
        return ans
    else:
        return sets[0]


n = 6
s = [1, 2, 3, 50, 7, 6]
ans_s = 0
count = 0
# Subset
while ans_s != 103:
    count += 1
    sub_s = [1, 2, 6, 7, 50]
    print(sub_s)
    gp_sz = random.randint(2, len(sub_s))
    print(gp_sz)
    gp = []
    print('------')
    while len(sub_s) > gp_sz:
        rem = random.sample(sub_s, gp_sz)
        print(rem)
        for val in rem:
            sub_s.remove(val)
        print(sub_s)
        gp.append(rem)
        print('------')

    print(gp)
    gp_ans = []
    for subby in gp:
        gp_ans.append(algebra(subby, gp_sz))

    print(sub_s)
    gp_ans.append(algebra(sub_s, len(sub_s)))
    print(gp_ans)

    ans_s = algebra(gp_ans, len(gp_ans))
    print(ans_s)
    print(count)
