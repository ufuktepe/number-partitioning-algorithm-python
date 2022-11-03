import sys

import copy
import math
import random
import time

from max_heap import MaxHeap
import utils_prepartition as pp
import utils_standard as std


MAX_ITER = 25000
N = 100


def kk(a):
    a_local = [*a]
    H = MaxHeap(a_local)
    n = len(a_local)

    for i in range(n-1):
        x = H.extract_max()
        y = H.extract_max()
        d = x - y
        H.insert(d)

    u = H.extract_max()
    return u


def repeated_random_std(a, init_solution=None):
    if init_solution is None:
        solution = std.generate_solution(N)
    else:
        solution = init_solution

    residue = std.calc_residue(a, solution)
    for i in range(MAX_ITER):
        new_solution = std.generate_solution(N)
        new_residue = std.calc_residue(a, new_solution)
        if new_residue < residue:
            residue = new_residue

    return residue


def repeated_random_pp(a, init_solution=None):
    if init_solution is None:
        solution = pp.generate_solution(N)
    else:
        solution = init_solution

    residue = kk(pp.prepartition(a, solution, N))
    for i in range(MAX_ITER):
        new_solution = pp.generate_solution(N)
        new_residue = kk(pp.prepartition(a, new_solution, N))
        if new_residue < residue:
            residue = new_residue

    return residue


def hill_climbing_std(a, init_solution=None):
    if init_solution is None:
        solution = std.generate_solution(N)
    else:
        solution = init_solution

    residue = std.calc_residue(a, solution)
    for i in range(MAX_ITER):
        new_solution = std.generate_neighbor(solution, N)
        new_residue = std.calc_residue(a, new_solution)
        if new_residue < residue:
            residue = new_residue
            solution = new_solution

    return residue


def hill_climbing_pp(a, init_solution=None):
    if init_solution is None:
        solution = pp.generate_solution(N)
    else:
        solution = init_solution

    residue = kk(pp.prepartition(a, solution, N))
    for i in range(MAX_ITER):
        new_solution = pp.generate_neighbor(solution, N)
        new_residue = kk(pp.prepartition(a, new_solution, N))
        if new_residue < residue:
            residue = new_residue
            solution = new_solution

    return residue


def simulated_annealing_std(a, init_solution=None):
    if init_solution is None:
        solution = std.generate_solution(N)
    else:
        solution = init_solution

    residue = std.calc_residue(a, solution)
    residue_global = residue
    for i in range(MAX_ITER):
        new_solution = std.generate_neighbor(solution, N)
        new_residue = std.calc_residue(a, new_solution)
        if new_residue < residue:
            residue = new_residue
            solution = new_solution
        elif random.random() < math.exp(-1 * (new_residue - residue) / temperature(i)):
            residue = new_residue
            solution = new_solution

        if residue_global > residue:
            residue_global = residue

    return residue_global


def simulated_annealing_pp(a, init_solution=None):
    if init_solution is None:
        solution = pp.generate_solution(N)
    else:
        solution = init_solution

    residue = kk(pp.prepartition(a, solution, N))
    residue_global = residue
    for i in range(MAX_ITER):
        new_solution = pp.generate_neighbor(solution, N)
        new_residue = kk(pp.prepartition(a, new_solution, N))
        if new_residue < residue:
            residue = new_residue
            solution = new_solution
        elif random.random() < math.exp(-1 * (new_residue - residue) / temperature(i)):
            residue = new_residue
            solution = new_solution

        if residue_global > residue:
            residue_global = residue

    return residue_global


def temperature(i):
    return (10 ** 10) * (0.8 ** math.floor(i / 300))


def run():
    n_args = len(sys.argv)

    if n_args != 4:
        print('Please provide the following parameters: flag algorithm inputfile')
        return

    flag = int(sys.argv[1])
    algo = int(sys.argv[2])
    inputfile = sys.argv[3]

    with open(inputfile, "r") as f:
        contents = f.readlines()
    a = []
    for item in contents:
        a.append(int(item))

    if algo == 0:
        res = kk(a)
        print(res)
        return res
    elif algo == 1:
        res = repeated_random_std(a)
        print(res)
        return res
    elif algo == 2:
        res = hill_climbing_std(a)
        print(res)
        return res
    elif algo == 3:
        res = simulated_annealing_std(a)
        print(res)
        return res
    elif algo == 11:
        res = repeated_random_pp(a)
        print(res)
        return res
    elif algo == 12:
        res = hill_climbing_pp(a)
        print(res)
        return res
    elif algo == 13:
        res = simulated_annealing_pp(a)
        print(res)
        return res


if __name__ == '__main__':
    run()



