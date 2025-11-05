from collections import defaultdict
class Node:
    def __init__(self, name, is_red=False):
        self.name = name,
        self.is_red = is_red
        self.edges : dict[Node : int] = defaultdict(int)
    
    def add_edge(self, to):
        self.update_edge(to, 1)

    def update_edge(self, to, weight):
        self.edges[to] += weight

class Graph:
    def __init__(self, n, r, s, t):
        self.n = n
        self.r = r
        self.s = s
        self.t = t