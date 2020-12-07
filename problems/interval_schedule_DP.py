import json


class Interval:
    def __init__(self, s, e, v):
        self.start_time = s
        self.end_time = e
        self.value = v

    def __str__(self):
        return 'start time:' + str(self.start_time) + ', end time:' + str(self.end_time) + ', value:' + str(self.value)


class Res:
    def __init__(self, s, v):
        self.seq = s
        self.value = v

    def __str__(self):
        return 'seq:' + str([str(i) for i in self.seq]) + '\nvalue:' + str(self.value)


def get_data_from_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    res = []
    for i in data['i']:
        res.append(Interval(i[0], i[1], i[2]))
    for i in range(len(res)):
        for j in range(len(res) - i - 1):
            if res[j].end_time > res[j + 1].end_time:
                tmp = res[j]
                res[j] = res[j + 1]
                res[j + 1] = tmp
    return res, data['time'][0], data['time'][1]


def DP(S, E, SEQ):
    if len(SEQ) <= 0:
        return Res([], 0)
    seq = []
    max_value = 0
    for i in range(len(SEQ)):
        if SEQ[i].start_time >= S:
            if SEQ[i].start_time < SEQ[0].end_time and i + 1 <= len(SEQ):
                curr_res = DP(SEQ[i].end_time, E, SEQ[i + 1:])
                curr_res.value += SEQ[i].value
            else:
                break
            if curr_res.value > max_value:
                seq = curr_res.seq + [SEQ[i]]
                max_value = curr_res.value
    return Res(seq, max_value)


if __name__ == '__main__':
    I, start_time, end_time = get_data_from_file('../test/ISDP2.json')
    r = DP(start_time, end_time, I)
    print(r)
