# aldes_red_scare
This is the repository for our red_scare algorithm design assignment

# Problems
## None
### Description
*Return the length of the shortest s,t-path*

### Strategy
Remove $R - \{s,t\}$ from $V(G)$  
*Probably if statement to ignore reds when queuing*  
`BFS(s,t)`

### Analysis
$O(V+E)$  


## Some
### Description
*Return whether there is a path from s to t that includes a vertex from R (true/false)*

### Strategy
We don't can't solve might be 

### Analysis


## Many
### Description
*Return the maximum number of red vertices on any path from s to t*

### Strategy
This is probably a longest path kinda deal


### Analysis
Reduction to longest path (NP-hard baby)

## Few
### Description
*Find any path with minimum reds*

### Strategy
Dijkstra with all black having cost 0 and reds having 1 

### Analysis
$O(V^2)$

## Alternate

### Description
*Return whether there is a path form s to t that alternates between red and non-red vertices (true/false)*

### Strategy
`BFS(s,t)`
with if statement that checks if next is alternate color?

### Analysis
$O(V+E)$
