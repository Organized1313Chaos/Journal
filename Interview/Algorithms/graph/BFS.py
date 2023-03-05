'''
Type 2: 
Graph Type: Directed (Multiple outgoing edge, no self loop)
Representation: An array of tuple (source, destination, weight)
Vertices: Indexes
Edges: (source, destination, weight) 
Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
'''

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        from collections import defaultdict
        graph = defaultdict(dict)
        
        for s, d, price in flights:
            graph[s][d] = price
            
        graph = dict(graph)
        dist = [float('inf') for _ in range(n)]
        
        q = [(src, 0)]
        stops = 0

        while stops <= k and q:
            sz = len(q)
            while sz > 0:
                sz -= 1
                node, distance = q.pop(0)
                if node not in graph:
                    continue
                for neighbour in graph[node]:
                    price = graph[node][neighbour]
                    if price + distance >= dist[neighbour]:
                        continue
                    dist[neighbour] = price + distance
                    q.append((neighbour, dist[neighbour]))
                
            stops += 1
        
        return dist[dst] if dist[dst] != float('inf') else -1
    

# ======================================================================

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
        