# Countdown Game
import random
import statistics
import pandas as pd
import numpy as np


def rand_select(val):
    n = random.choice([1, 2, 3, 4, 5, 6])
    sel = random.sample(val, n)
    return n, sel


def sel_operations(N):
    ops = random.sample([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4], N-1)
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


target = 373
values = [97, 2, 3, 5, 13, 7]
sample_sz = 5
sample = []
solutions = []
for run in range(sample_sz):
    trials = 1
    ans = 0
    while ans != target:
        [sz, v] = rand_select(values)
        print(v)
        v_save = list(np.copy(v))
        operations = sel_operations(sz)
        print(operations)
        if operations != []:
            for i in range(sz-1):
                if operations[i] == 1:
                    ans = add(v[i], v[i+1])
                elif operations[i] == 2:
                    ans = sub(v[i], v[i+1])
                elif operations[i] == 3:
                    ans = mult(v[i], v[i+1])
                else:
                    ans = div(v[i], v[i+1])
                v[i+1] = ans
        else:
            ans = v[0]
        print(trials)
        print(ans)
        if ans == target:
            group = [v_save, operations]
            solutions.append(group)
            print('YES')
            break
        else:
            print('NO')
        trials += 1

    sample.append(trials)

print(sample)
print(statistics.mean(sample))
print(statistics.median(sample))
print(solutions)
