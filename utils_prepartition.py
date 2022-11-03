import random


def generate_solution(n):
    return [random.randrange(n) for p in range(n)]

def prepartition(a, solution, n):
    new_a = [0] * n
    for i in range(n):
        new_a[solution[i]] += a[i]

    return [i for i in new_a if i != 0]


def generate_neighbor(solution, n):
    neighbor_solution = [*solution]
    i = random.randrange(n)
    j = random.randrange(n)
    while neighbor_solution[i] == j:
        j = random.randrange(n)
    neighbor_solution[i] = j
    return neighbor_solution


if __name__ == '__main__':
    pass

