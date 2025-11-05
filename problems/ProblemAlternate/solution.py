from graph_utils.graphs import *
from graph_utils.read_input import read_graph
from algorithms.bfs import bfs
g : Graph = read_graph()

print(bfs(g.s, g.t, predicate=(lambda n1, n2: n1.is_red != n2.is_red)) is not None)
    