'''
- Bellman Ford's algorithm is used to find the shortest paths from the source\
node to all other vertices in a weighted graph. 
- It depends on the idea that the shortest path contains at most N - 1 edges\
because the shortest path cannot have a cycle.

Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/2825208/cheapest-flights-within-k-stops/

Time complexity: O((N+E)*K)
Space complexity: O(N)
Paradigm: Dynamic Programming
'''

# The solution is about shortest distance between two nodes
# with at most k stops
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        # Distance from source to all other nodes.
        dist = [float('inf')] * n
        dist[src] = 0

        # Run only K+1 times since we want shortest distance in K hops.
        for i in range(k+1):
            # Create a copy of dist list.
            temp = dist.copy()
            for flight in flights:
                if dist[flight[0]] != float('inf'):
                    temp[flight[1]] = min(temp[flight[1]], dist[flight[0]] + flight[2])
            # Copy the temp list into dist.
            dist = temp
        return dist[dst] if dist[dst] != float('inf') else -1
