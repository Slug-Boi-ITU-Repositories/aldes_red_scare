from graph_utils.graphs import *

def read_graph():
    N,M,_ = map(int, input().split())

    s, t = input().split()

    v : dict[str, Node] = {}
    r : dict[str, Node] = {}

    for _ in range(N):
        n = input().split()
        if len(n) > 1:
            node = Node(n[0], True)
            r[n[0]] = node
        else:
            node = Node(n[0])

        v[n[0]] = node
        

    for _ in range(M):
        e = input().split()
        if e[1] == '--':
            v[e[0]].add_edge(v[e[2]])
            v[e[2]].add_edge(v[e[0]])
        else:
            v[e[0]].add_edge(v[e[2]])

    return Graph(v, r, v[s], v[t])