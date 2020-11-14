import copy


class Good:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __str__(self):
        return 'weight:' + str(self.weight) + ' value:' + str(self.value)

    def ratio(self):
        return self.value / self.weight


def bubble(l):
    for i in range(len(l)):
        j = 0
        while j + i < len(l) - 1:
            if l[j].ratio() < l[j + 1].ratio():
                tmp = copy.deepcopy(l[j])
                l[j] = l[j + 1]
                l[j + 1] = tmp
            j += 1


def get_data_from_file(filename):
    all_goods = []
    with open(filename)as f:
        values = f.readline()[:-1].split(' ')
        weights = f.readline()[:-1].split(' ')
        capacities = int(f.readline())
    for i in range(len(values)):
        all_goods.append(Good(int(weights[i]), int(values[i])))
    bubble(all_goods)
    return all_goods, capacities


if __name__ == '__main__':
    filename = '../test/knapsack.txt'
    goods, capacities = get_data_from_file(filename)
    for i in goods:
        print(i.ratio())
