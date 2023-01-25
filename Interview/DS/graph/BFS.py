'''
Type 1: 
Graph Type: Directed (Single outgoing edge)
Representation: An array
Vertices: Indexes
Edges: Values (Outgoing Edge)
Link: https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
'''


edges = [2,2,3,-1]
N = len(edges)
def BFS(start):
    q = [start]
    # Matrix that store distance from one node to other
    distances = [float('inf') for _ in range(N)]
    
    visited = set()
    depth = 0
    
    while q:
        node = q.pop(0)
        if node==-1: break
        
        visited.add(node)
        distances[node] = depth
        
        nbrs = edges[node]    
        
        if nbrs not in visited:
            q.append(nbrs)
        
        depth +=1

    return distances
        