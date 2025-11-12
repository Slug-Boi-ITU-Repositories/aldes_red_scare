from graph_utils.graphs import *
from graph_utils.read_input import read_graph
from algorithms.somepath import some_path

g : Graph = read_graph()
print(some_path(g.s, g.t))