import copy


def get_data_from_file(filename):
    with open(filename, 'r')as f:
        return list(map(int, f.readline()[:-1].split(' ')))


def get_min(L):
    if len(L) == 0:
        return (10000, 10000)
    min_num = L[0]
    for i in range(1, len(L)):
        if min_num[1] > L[i][1]:
            min_num = L[i]
    return min_num


if __name__ == "__main__":
    l = get_data_from_file("../test/kth_small")
    k = l[0]
    l.remove(k)
    seq = []
    for i in range(len(l)):
        seq.append((i + 1, l[i]))
    seqs = []
    j = 0
    length = int(len(seq) / k)
    for i in range(k - 1):
        seqs.append(seq[j:j + length])
        j += length
    seqs.append(seq[j:])
    for i in range(k):
        kth_min = get_min(seqs[0])
        pos = 0
        for j in range(len(seqs)):
            curr_min = get_min(seqs[j])
            if kth_min[1] > curr_min[1]:
                kth_min = curr_min
                pos = j
        seqs[pos].remove(kth_min)
        if [] in seqs:
            seqs.remove([])
    print("Position: "+str(kth_min[0])+" number: "+str(kth_min[1]))
