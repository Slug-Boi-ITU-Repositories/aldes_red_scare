from graph_utils.graphs import *
from graph_utils.read_input import read_graph
from algorithms.dijkstras import djikstra

g : Graph = read_graph()

print(djikstra(g.s, g.t))
