from graph_utils.graphs import *
from graph_utils.read_input import read_graph

g : Graph = read_graph()
print(len(g.n), len(g.r), g.s.name, g.t.name)
