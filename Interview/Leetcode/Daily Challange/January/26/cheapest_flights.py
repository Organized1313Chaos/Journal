# ====================================================
'''
Leetcode Question
Date: January 26, 2023
Problem Number: 787 
Name: Cheapest Flights Within K Stops
Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
'''
# ====================================================

'''
Approach 1: Partially Successful Approach, BFS
No of Test Cases Passed: 41/54
'''

'''
NOTES:
pass

MISTAKES:
if you append a copy of list (mutable objects)
Ensure that you store a copy instead of reference

Time Complexity: O(|V|+|E|)
Space Complexity: O(|V|)
'''
# ====================================================
# class Solution:
#     def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
#         from collections import defaultdict
        
#         graph = defaultdict(dict)
        
#         for s, d, price in flights:
#             graph[s][d] = price
            
#         graph = dict(graph)
        
#         #BFS
#         visited = set()
#         q = [(src, 0)]
        
#         # price_mat = [float('inf')]*n

#         output = float('inf')
        
#         for  _ in range(k+2):
#             new_level = []
#             while q:
#                 node, price = q.pop(0)
                
#                 if node == dst:
#                     output = min(output, price)
                    
#                 visited.add(node)
                
#                 if node not in graph:
#                     continue
                
#                 for nbrs in graph[node]:
#                     if nbrs in visited:
#                         continue
#                     # new_price =  min( price+graph[node][nbrs], price_mat[node]) 
#                     # price_mat[node] = price+graph[node][nbrs]
#                     new_level.append( ( nbrs, price+graph[node][nbrs] ) )
                
#             q = new_level
        
#         if output==float('inf'):
#             return -1
        
#         return output

# =====================================================================
# TestCases
# Sample Test Case 1

# sol = Solution()
# n = 4
# flights = [[0,1,100,],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
# src = 0
# dst = 3
# k = 1
# res = sol.findCheapestPrice( n, flights, src, dst, k)
# print(f"res={res}")

# ======================================================================
# Failed Test Case


'''
Approach 2: Partially Successful Approach, BFS
No of Test Cases Passed: 41/54
Updated: instead of node in visited, I added (node, next_node)
Failed Test Case Passed, but other failed
'''


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        from collections import defaultdict
        
        graph = defaultdict(dict)
        
        for s, d, price in flights:
            graph[s][d] = price
            
        graph = dict(graph)
        
        #BFS
        q = [(src, 0)]
        visited = set()
        
        price_mat = [float('inf')]*(n+1)
        output = float('inf')
        
        for  _ in range(k+2):
            new_level = []
            while q:
                node, price = q.pop(0)
                new_price =  min( price, price_mat[node]) 
                price_mat[node] = new_price
                
                if node == dst:
                    output = min(output, price_mat[node])
                
                if node not in graph:
                    continue
                
                for nbrs in graph[node]:
                    if (node, nbrs) in visited:
                        continue
                    new_price =  min( price+graph[node][nbrs], price_mat[node]) 
                    price_mat[node] = price+graph[node][nbrs]
                    new_level.append( ( nbrs, price+graph[node][nbrs] ) )
                    visited.add( (node, nbrs) )
                
            q = new_level
        
        if output==float('inf'):
            return -1
        
        return output



sol = Solution()
n = 5
flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
src = 0
dst = 2
k = 2
res = sol.findCheapestPrice( n, flights, src, dst, k)
print(f"res={res}")

# Reason: Failure due to directed cyclings

# =================================================

# Solution Copied from Leetcode

'''
Approach 3: Successful Approach, BFS
No of Test Cases Passed: 54/54
Updated: Execution Error Coorection
Corrections: Time & Space Complexity: O(N+E*K)
'''


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
    