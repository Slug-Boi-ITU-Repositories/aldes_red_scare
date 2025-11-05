from graph_utils.graphs import *
from graph_utils.read_input import read_graph
from algorithms.bfs import bfs
g : Graph = read_graph()

edge_from = bfs(g.s, g.t, predicate=(lambda _, n2: not n2.is_red))
if edge_from is None:
    print(-1)
else:
    res = 0
    n = g.t
    while n in edge_from:
        res +=1
        n = edge_from[n]

    print(res)
    