from graph_utils.graphs import *
from graph_utils.read_input import read_graph
from algorithms.longestpath import longest_path

g : Graph = read_graph()
print(longest_path(g.s, g.t))