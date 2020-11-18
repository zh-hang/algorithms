import copy
from TSP import get_data_from_file
from TSP import get_dis


def get_low_bound(R, C):
    lb = 0
    min_dis = 10000
    if len(C) > 0:
        for i in R[0].in_neighbours:
            if i[0] in [j.name for j in C]:
                if i[1] < min_dis:
                    min_dis = i[1]
        lb += min_dis
    for i in range(1, len(R)):
        lb += R[i - 1].get_out_neighbour_dis(R[i].name) * 2
    min_dis = 10000
    if len(C) > 0:
        for i in R[-1].out_neighbours:
            if i[0] in [j.name for j in C]:
                if i[1] < min_dis:
                    min_dis = i[1]
        lb += min_dis
    for i in range(len(C)):
        min_dis = 10000
        for j in C[i].out_neighbours:
            if j[1] < min_dis:
                min_dis = j[1]
        if min_dis == 10000:
            print("error!")
        lb += min_dis
        min_dis = 10000
        for j in C[i].in_neighbours:
            if j[1] < min_dis:
                min_dis = j[1]
        if min_dis == 10000:
            print("error!")
        lb += min_dis
    return lb / 2


def has_traversal(R, c):
    for i in R:
        if i.name == c:
            return True
    return False


def BB(R, C):
    if len(C) == 0:
        return R
    lb1 = 10000
    first = True
    R1 = copy.deepcopy(R)
    C1 = []
    for i in R[-1].out_neighbours:
        for j in C:
            if j in R:
                continue
            if i[0] == j.name:
                R.append(j)
                tmp = copy.deepcopy(C)
                tmp.remove(j)
                curr_lb = get_low_bound(R, tmp)
                if lb1 > curr_lb:
                    lb1 = curr_lb
                    if not first:
                        R1.pop()
                    first = False
                    R1.append(j)
                    C1 = copy.deepcopy(tmp)
                R.pop()
                break
    return BB(R1, C1)


if __name__ == '__main__':
    cities = get_data_from_file('../test/TSP.txt')
    R = BB([cities[0]], cities[1:])
    R.append(cities[0])
    for i in R:
        print(i.name, end=' ')
    print('\nThe distance is', end=' ')
    print(get_dis(R))
