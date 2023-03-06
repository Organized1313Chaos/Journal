# ====================================================
'''
Leetcode Question
Date: March 5, 2023
Problem Number: 1345
Name:  Jump Game IV
Link: https://leetcode.com/problems/jump-game-iv/
Solution Link: https://leetcode.com/problems/jump-game-iv/solutions/3257846/day-64-bfs-o-n-time-and-o-n-space-easiest-beginner-friendly-sol/
'''
# ====================================================

'''
Approach 1: Partially Successful Approach, Backtracking
Paradigm: Backtracking algorithm, DP
- 
No of Test Cases Passed: 22/33
'''

'''
NOTES:
pass

MISTAKES:
pass

Time Complexity: 
Space Complexity:
'''
# ====================================================

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        from collections import defaultdict
        N = len(arr)
        if N==1: return 0

        lookup = defaultdict(set)

        for index, value in enumerate(arr):
            lookup[value].add(index)
        
        # print(lookup)
        dp = [float('inf')]*N
        dp[0] = 0

        def helper(start, dp, step):
            if start-1>=0:
                dp[start-1] = min(dp[start-1], step+1)
                if dp[start-1]==step+1:
                    helper(start-1, dp, step+1)
                
            if start+1<N:
                dp[start+1] = min(dp[start+1], step+1)
                if dp[start+1]==step+1:
                    helper(start+1, dp, step+1)

            
            val = arr[start]
            for j in lookup[val]:
                dp[j] = min(dp[j], step+1)
                if dp[j]==step+1:
                    helper(j, dp, step+1)
        helper(0, dp, 0)

        return dp[-1]

# ====================================================

sol = Solution()
arr = [100,-23,-23,404,100,23,23,23,3,404]
res = sol.minJumps(arr)
print(f"res={res}")

# =====================================================

'''
Note: Sometimes BFS gies you huristic approaches
That approaches to solution quicker than expected.
'''
from collections import defaultdict

class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        
        indices = defaultdict(list)
        for i in range(n):
            indices[arr[i]].append(i)
        
        storeIndex = deque()
        visited = [False] * n
        storeIndex.append(0)
        visited[0] = True
        steps = 0
        
        while storeIndex:
            size = len(storeIndex)
            while size > 0:
                currIndex = storeIndex.popleft()
                size -= 1
                if currIndex == n - 1:
                    return steps
                
                jumpNextIndices = indices[arr[currIndex]]
                jumpNextIndices.append(currIndex - 1)
                jumpNextIndices.append(currIndex + 1)
                for jumpNextIndex in jumpNextIndices:
                    if 0 <= jumpNextIndex < n and not visited[jumpNextIndex]:
                        storeIndex.append(jumpNextIndex)
                        visited[jumpNextIndex] = True
                jumpNextIndices.clear()
            steps += 1
        return -1

