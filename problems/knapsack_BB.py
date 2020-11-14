import copy
from knapsack import get_data_from_file


def edge(good, ub, capacity):
    return ub + capacity / good.ratio()


def calculate_value(g):
    sum = 0
    for i in g:
        sum += i.value
    return sum


def calculate_weight(g):
    sum = 0
    for i in g:
        sum += i.weight
    return sum


def BB(g, n, c, k):
    if n >= len(g):
        return k
    k1 = copy.deepcopy(k)
    k1.append(g[n])
    if capacity - calculate_weight(k1) >= 0:
        ub1 = edge(g[n + 1], calculate_value(k1), c - calculate_weight(k1))
        ub2 = edge(g[n + 1], calculate_value(k), c - calculate_weight(k))
        if ub1 >= ub2:
            return BB(g, n + 1, c, k1)
    return BB(g, n + 1, c, k)


if __name__ == '__main__':
    goods, capacity = get_data_from_file('../test/knapsack.txt')
    knap = BB(goods, 0, capacity, [])
    for i in knap:
        print(i)
    print(calculate_value(knap))
