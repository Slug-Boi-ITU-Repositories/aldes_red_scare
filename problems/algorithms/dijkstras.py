from graph_utils.graphs import *
from queue import PriorityQueue
import math
from collections import defaultdict

# I rate this +1                                             
def djikstra(s : Node, t : Node):
    pq : PriorityQueue[tuple[int, Node]] = PriorityQueue()
    pq.put((0, s))
    seen = set()
    edge_from = {}
    dist_to = defaultdict(lambda: math.inf)
    dist_to[s] = 0
    while not pq.empty():
        n = pq.get()[1]
        if n == t:
            return dist_to[t] if not t.is_red else dist_to[t] - 1
        seen.add(n)
        for node_to in n.edges.keys():
            w = 1 if node_to.is_red else 0
            if node_to not in seen and dist_to[n] + w < dist_to[node_to]:
                dist_to[node_to] = dist_to[n] + w
                edge_from[node_to] = n
                pq.put((dist_to[node_to], node_to))
    return -1
            
    