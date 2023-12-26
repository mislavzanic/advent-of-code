from aoc_util.advent import Input
import networkx as nx

def p1(day: Input):
    G = nx.Graph()
    for line in day.lines():
        start, ends = line.split(': ')
        ends = ends.split(' ')
        G.add_node(start)
        for end in ends:
            G.add_node(end)
            G.add_edge(start, end)
    s = nx.minimum_edge_cut(G)

    for item in s:
        G.remove_edge(*item)

    w1 = list(nx.connected_components(G))
    return len(w1[0]) * len(w1[1])
