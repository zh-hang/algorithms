import copy
from knapsack import Good
from knapsack import get_data_from_file


def is_over_flow(V, capacities):
    s = 0
    for i in V:
        s += i.weight
    if s > capacities:
        return True
    return False


def comp_k(k1, k2):
    v1 = 0
    v2 = 0
    for i in k1:
        v1 += i.value
    for i in k2:
        v2 += i.value
    if v1 >= v2:
        return k1
    return k2


def DFS(G, K, capacities):
    if len(G) == 0:
        return K
    k1 = copy.deepcopy(K)
    k1.append(G[0])
    if is_over_flow(k1, capacities):
        k1.pop()
    k1 = DFS(G[1:], k1, capacities)
    k2 = copy.deepcopy(K)
    k2 = DFS(G[1:], k2, capacities)
    return comp_k(k1, k2)


if __name__ == '__main__':
    filename = '../test/knapsack.txt'
    goods, capacities = get_data_from_file(filename)
    r = DFS(goods, [], capacities)
    print('Result is following:')
    v = 0
    for i in r:
        print(i)
        v += i.value
    print('value: ' + str(v))
