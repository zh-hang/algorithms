from knapsack import get_data_from_file
import copy


class Knap:
    def __init__(self, G, value):
        self.goods = G
        self.value = value

    def __str__(self):
        return 'goods:' + str([str(i) for i in self.goods]) + '\nvalue:' + str(self.value)


def DP(Goods, Capacities):
    if len(Goods) <= 0:
        return Knap([], 0)
    G = copy.deepcopy(Goods)
    goods = []
    max_value = 0
    while len(G) > 0:
        g = G.pop()
        curr_k = Knap([], 0)
        if Capacities - g.weight >= 0:
            curr_k = DP(G, Capacities - g.weight)
            curr_k.value += g.value
        if curr_k.value > max_value:
            goods = curr_k.goods + [g]
            max_value = curr_k.value
    return Knap(goods, max_value)


if __name__ == '__main__':
    filename = '../test/knapsack.txt'
    goods, capacities = get_data_from_file(filename)
    k = DP(goods, capacities)
    print(k)
