class Good:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __str__(self):
        return 'weight:' + str(self.weight) + ' value:' + str(self.value)


def get_data_from_file(filename):
    all_goods = []
    with open(filename)as f:
        values = f.readline()[:-1].split(' ')
        weights = f.readline()[:-1].split(' ')
        capacities = int(f.readline())
    for i in range(len(values)):
        all_goods.append(Good(int(weights[i]), int(values[i])))
    return all_goods, capacities
