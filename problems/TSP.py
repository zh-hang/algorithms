import copy

city_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


class City:
    def __init__(self, out_neighbours):
        self.out_neighbours = []
        self.in_neighbours = []
        self.name = ''
        for i in range(len(out_neighbours)):
            if out_neighbours[i] == '0':
                self.name = city_names[i]
                continue
            self.out_neighbours.append((city_names[i], int(out_neighbours[i])))

    def get_in_neighbours(self, in_neighbour):
        self.in_neighbours.append(in_neighbour)

    def __eq__(self, other):
        if self.name == other.name:
            if self.out_neighbours == other.out_neighbours:
                return True

    def __str__(self):
        return 'name: ' + self.name + ', in neighbours' + str(self.in_neighbours) + ', out neighbours:' + str(
            self.out_neighbours)

    def get_out_neighbour_dis(self, neighbour):
        for i in self.out_neighbours:
            if i[0] == neighbour:
                return i[1]
        print("error!")


def get_data_from_file(filename):
    cities = []
    with open(filename)as f:
        l = f.readline()
        while l != '':
            d = l.split(' ')
            cities.append(City(d))
            l = f.readline()
    for i in cities:
        for j in i.out_neighbours:
            for k in cities:
                if j[0] == k.name:
                    k.get_in_neighbours((i.name, j[1]))
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
    for i in range(len(R) - 1):
        dis += R[i].get_out_neighbour_dis(R[i + 1].name)
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
    RR = comp_dis(R)
    for i in RR:
        print(i.name, end=' ')
    print('\nThe distance is', end=' ')
    print(get_dis(RR))
