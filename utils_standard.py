import random


def calc_residue(a, solution):
    return abs(sum([(a * s) for a, s in zip(a, solution)]))

def generate_solution(n):
    return [1 if random.random() < 0.5 else -1 for i in range(n)]


def generate_neighbor(solution, n):
    neighbor_solution = [*solution]
    i = random.randrange(n)
    j = random.randrange(n)
    while i == j:
        j = random.randrange(n)
    neighbor_solution[i] *= -1
    if random.uniform(0, 1) < 0.5:
        neighbor_solution[j] *= -1
    return neighbor_solution


if __name__ == '__main__':
    pass

