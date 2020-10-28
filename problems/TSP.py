import copy

city_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


class City:
    def __init__(self, neighbours):
        self.neighbours = []
        self.name = ''
        for i in range(len(neighbours)):
            if neighbours[i] == '0':
                self.name = city_names[i]
                continue
            self.neighbours.append((city_names[i], int(neighbours[i])))

    def __eq__(self, other):
        if self.name == other.name:
            if self.neighbours == other.neighbours:
                return True

    def __str__(self):
        return 'name:' + self.name + ' neighbours:' + str(self.neighbours)

    def get_neighbour_dis(self, neighbour):
        for i in self.neighbours:
            if i[0] == neighbour:
                return i[1]


def get_data_from_file(filename):
    cities = []
    with open(filename)as f:
        l = f.readline()
        while l != '':
            d = l.split(' ')
            cities.append(City(d))
            l = f.readline()
    return cities


def get_next(G, R):
    for i in G:
        if i.name not in R:
            return R.append[i.name]
    return R


def get_all_routes(G, R):
    NR = []
    isOver = True
    for i in R:
        for j in G:
            if j not in i:
                tmp = copy.deepcopy(i)
                tmp.append(j)
                NR.append(tmp)
                isOver = False
    if isOver:
        return R
    return get_all_routes(G, NR)


def get_dis(R):
    dis = 0
    for i in range(len(R)-1):
        dis += R[i].get_neighbour_dis(R[i + 1].name)
    return dis


def comp_dis(R):
    dis = 1000
    RR = []
    for i in R:
        if get_dis(i) < dis:
            RR = i
            dis = get_dis(i)
    return RR


if __name__ == '__main__':
    cities = get_data_from_file('../test/TSP.txt')
    R = get_all_routes(cities, [[cities[0]]])
    for i in R:
        i.append(cities[0])
    RR =comp_dis(R)
    for i in RR:
        print(i.name, end=' ')
