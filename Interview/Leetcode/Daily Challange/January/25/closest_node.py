# ====================================================
'''
Leetcode Question
Date: January 25, 2023
Problem Number: 2359
Name:  Find Closest Node to Given Two Nodes
Link: https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/
'''
# ====================================================

'''
Approach 1: Succcessfull Approach, BFS
- Run BFS and store distances from node to each node using BFS
- For each node calculate the maximum and update the global minimum of such distance
No of Test Cases Passed: 70/77 (Stage 1)

False Edge Case: if start and end are same then return 0 
Reason of Failure: Whenever there are undirected edges do not make assumption 
That minimum of such distance will be 0 

No of Test Cases Passed: 77/77 (Stage 2)

Time Complexity: O(|V|)
Space Complexity: O(|V|)
'''

'''
NOTES:
pass

MISTAKES:
pass
'''
# ====================================================


class Solution:
    
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        
        # if node1==node2: return 0
        N = len(edges)
        
        #BFS
        def BFS(start):
            q = [start]
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
        
        dist1 = BFS(node1)
        dist2 = BFS(node2)
        
        ans = float('inf')
        output = -1
        
        print(dist1)
        print(dist2)
        
        for index, val1 in enumerate(dist1):
            if val1 == float('inf'):
                continue
            val2 = dist2[index]
            if val2 == float('inf'):
                continue
            tp = max(val1, val2)
            if tp < ans:
                ans = tp
                output = index
                
        return output   
            
    
sol = Solution()
edges = [2,2,3,-1]
node1 = 0
node2 = 1
res = sol.closestMeetingNode(edges, node1, node2)
print(f"res={res}")