import copy
import networkx as nx
import matplotlib.pyplot as plt

colors = ('grey', 'red', 'tan', 'gold', 'y', 'sage', 'g', 'lime', 'teal', 'c', 'b', 'plum', 'pink')
nodes_name = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K')


class Node:
    def __init__(self, name, neighbours):
        self.color = None
        self.name = name
        self.neighbours = neighbours

    def __str__(self):
        return 'name' + str(self.name) + ' color:' + str(self.color) + ' neighbours:' + str(self.neighbours)

    def get_neighbour(self, neighbour_name, nodes):
        if neighbour_name not in self.neighbours:
            return None
        for n in nodes:
            if neighbour_name == nodes[n].name:
                return nodes[n]
        return None


def get_data_from_file(file_path):
    nodes = {}
    with open(file_path) as f:
        l = f.readline()
        i = 0
        while l != '':
            row = l[:-1].split(' ')
            n = []
            for j in range(len(row)):
                if i == j:
                    continue
                if row[j] == '1':
                    n.append((nodes_name[j]))
            nodes[nodes_name[i]] = Node(nodes_name[i], n)
            i += 1
            l = f.readline()
    return nodes


def color(nodes, name_key, color_num):
    if nodes[name_key].color is not None:
        return
    neighbour_colors = []
    neighbours = []
    n = 0
    for i in nodes[name_key].neighbours:
        curr = nodes[name_key].get_neighbour(i, nodes)
        neighbours.append(copy.deepcopy(curr))
        if curr is not None:
            if curr.color is not None and curr.color not in neighbour_colors:
                neighbour_colors.append(curr.color)
                n += 1
    if n >= color_num:
        color_num = n + 1
        nodes[name_key].color = colors[color_num - 1]
    else:
        for i in range(color_num):
            if colors[i] in neighbour_colors:
                continue
            nodes[name_key].color = colors[i]
    for i in nodes[name_key].neighbours:
        color(nodes, i, color_num)
    return color_num


if __name__ == '__main__':
    nodes = get_data_from_file('../test/nondirectional_map.txt')
    k = 0
    color(nodes, 'A', k)
    G = nx.Graph()
    node_color = []
    for i in nodes:
        print(nodes[i])
        G.add_node(i)
        for j in nodes[i].neighbours:
            G.add_edge(i, j)
    for i in G:
        node_color.append(nodes[i].color)
    nx.draw(G, node_color=node_color, with_labels=True)
    plt.show()
