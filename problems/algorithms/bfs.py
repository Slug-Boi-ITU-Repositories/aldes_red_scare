from graph_utils.graphs import *
from queue import Queue

# I rate this +1
def bfs(G : Graph, s : Node, t : Node, predicate = (lambda nfrom, nto : True)):
    queue : Queue[Node] = Queue()
    queue.put(s)
    seen = set()
    edge_from = {}
    while queue.not_empty:
        n = queue.get()
        seen.add(n)
        for node_to in n.edges.keys():
            if node_to == t:
                edge_from[node_to] = n
                return edge_from
            
            if node_to not in seen and predicate(n, node_to):
                edge_from[node_to] = n
                queue.put(node_to)
    return None
            
    