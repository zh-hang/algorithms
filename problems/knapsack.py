import copy


class Good:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __str__(self):
        return 'weight:' + str(self.weight) + ' value:' + self.value


def is_over_flow(V, capacities):
    s = 0
    for i in V:
        s += i.weight
    if s > capacities:
        return True
    return False


def get_data_from_file(file_name):
    all_goods = []
    with open(file_name)as f:
        values = f.readline()
        weights = f.readline()
        values.split(' ')
        weights.split(' ')
        capacities = int(f.readline())
    for i in range(len(values)):
        all_goods.append(Good(weights[i], values[i]))
    return all_goods, capacities


def comp_k(k1, k2):
    v1 = 0
    v2 = 0
    for i in range(len(k1)):
        v1 += k1[i].value
        v2 += k2[i].value
    if v1 >= v2:
        return k1
    return k2


def DFS(G, K, capacities):
    if len(G) == 0:
        return K
    k1 = copy.deepcopy(K)
    if not is_over_flow(k1, capacities):
        k1.append(G[0])
        DFS(G[1:], k1, capacities)
    k2 = copy.deepcopy(K)
    DFS(k2)
    return comp_k(k1,k2)


if __name__ == '__main__':
    filename = '../test/knapsack.txt'
    goods, capacity = get_data_from_file(filename)
