import pprint
import numpy as np
import copy
in_data = list()
with open('formula.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        in_data.append(line)

cnf = list()
cnf.append(list())
maxvar = 0

for line in in_data:
    tokens = line.split()
    if len(tokens) != 0 and tokens[0] not in ("p"):
        for tok in tokens:
            lit = int(tok)
            maxvar = max(maxvar, abs(lit))
            if lit == 0:
                cnf.append(list())
            else:
                cnf[-1].append(lit)

assert len(cnf[-1]) == 0
cnf.pop()

max_len = max([len(sub) for sub in cnf])

matrix = list()
for sub in cnf:
    matrix.append(sub + [0] * (max_len - len(sub)))

matrix = np.array(sorted(matrix))

matrix_1 = copy.copy(matrix)


def replace_n(mtrx, n):
    mtrx = np.where(mtrx == n, -n, np.where(mtrx == -n, n, mtrx))
    return mtrx


matrix_2 = replace_n(matrix, 1671)
matrix_2 = np.sort(matrix, axis=1)
matrix_3 = matrix_1 - matrix_2

