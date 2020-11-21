import copy
import json


def get_data_from_file(filename):
    with open(filename)as f:
        seq = json.load(f)
        return seq


def get_reverse(seq):
    reverse = []
    if len(seq) > 2:
        sec = int(len(seq) / 2)
        s1 = copy.deepcopy(seq[0:sec])
        s2 = copy.deepcopy(seq[sec:])
        reverse1, s1 = get_reverse(s1)
        reverse2, s2 = get_reverse(s2)
        reverse += reverse1 + reverse2
        i1 = 0
        i2 = 0
        i = 0
        while i < len(seq):
            while i1 < len(s1) and s1[i1] <= s2[i2]:
                seq[i] = s1[i1]
                i += 1
                i1 += 1
            curr_i2 = i2
            if i1 >= len(s1) and i2 < len(s2):
                seq[-(len(s2) - i2):] = s2[i2:]
                break
            while i2 < len(s2) and s1[i1] > s2[i2]:
                seq[i] = s2[i2]
                i += 1
                i2 += 1
            for j in range(curr_i2, i2):
                curr_i1 = i1
                while curr_i1 < len(s1) and s1[curr_i1] > s2[j]:
                    reverse.append((s1[curr_i1], s2[j]))
                    curr_i1 += 1
            if i2 >= len(s2) and i1 < len(s1):
                seq[-(len(s1) - i1):] = s1[i1:]
                break
    elif len(seq) == 2:
        if seq[0] > seq[1]:
            reverse.append((seq[0], seq[1]))
            tmp = seq[0]
            seq[0] = seq[1]
            seq[1] = tmp
    return reverse, seq


if __name__ == '__main__':
    seq = get_data_from_file('../test/seq.txt')
    l = [1, 7, 15, 3, 9, 2]
    print(l)
    reverse, l = get_reverse(l)
    print(reverse)
    print(len(reverse))
    print(l)
