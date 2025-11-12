from graph_utils.graphs import *
import sys

sys.setrecursionlimit(80000)

def longest_path(start : Node, end : Node):
    def check_node(n : Node, checked : set[Node], reds):
        checked.add(n)
        if n.is_red:
            reds += 1
        if n == end:
            return reds
        res = -1
        for neighbour in n.edges:
            if not neighbour in checked:
                 new_res = check_node(neighbour, checked.copy(), reds)
                 res = new_res if new_res > res else res

        return res

    return check_node(start, set(), 0)

    
    
    