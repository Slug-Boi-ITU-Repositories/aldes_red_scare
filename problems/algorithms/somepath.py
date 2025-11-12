from graph_utils.graphs import *
import sys

sys.setrecursionlimit(80000)

def some_path(start : Node, end : Node):
    def check_node(n : Node, checked : set[Node], red):
        checked.add(n)
        if n.is_red:
            red = True
        if n == end:
            return red
        for neighbour in n.edges:
            if not neighbour in checked:
                 if check_node(neighbour, checked.copy(), red):
                     return True
                 
        return False
                 
    return check_node(start, set(), False)

    
    