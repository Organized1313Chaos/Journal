'''
Type 1: 
Graph Type: Directed (Single outgoing edge)
Representation: An array
Vertices: Indexes
Edges: Values (Outgoing Edge)
Link: https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
'''

'''
Note: We cannot use DFS in standard unweighted graph to find the shortest 
      distance from a node to any other node.
'''
edges = [2,2,3,-1]
N = len(edges)

dist1 = [float('inf')] * N
node1 = 1
visit1 = [False] * N

dist1[node1] = 0

class Solution:
    def dfs(self, node, edges, dist, visit):
        visit[node] = True
        neighbor = edges[node]
        if neighbor != -1 and not visit[neighbor]:
            dist[neighbor] = 1 + dist[node]
            self.dfs(neighbor, edges, dist, visit)