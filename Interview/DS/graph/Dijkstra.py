'''
Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/solutions/2825208/cheapest-flights-within-k-stops/

Time complexity: O(N + E*K*log(E*K))
Space complexity: O(N+E*K)
Paradigm: Greedy Algorithm
'''

## Dijkstras
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        from collections import defaultdict
        import heapq
        
        visited = {}
        adj = defaultdict(list)
        for s, d, p in flights:
            adj[s].append((d, p))
        pq = [(0, 0, src)]
        while pq:
            cost, stops, node = heapq.heappop(pq)
            if node == dst and stops - 1 <= k:
                return cost
            if node not in visited or visited[node] > stops:
                visited[node] = stops
                for neighbor, price in adj[node]:
                    heapq.heappush(pq, (cost + price, stops + 1, neighbor))
        return -1