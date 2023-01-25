# ====================================================
'''
Leetcode Question
Date: January 24, 2023
Problem Number: 909
Name: Snakes and Ladders
Link: https://leetcode.com/problems/snakes-and-ladders/description/
'''

'''
Approach 1: Failed Approach, Dynamic Prgrammin
- No Proper Execution
No of Test Cases Passed: N/A
'''

'''
Note: 
- While traversing backwards make sure you 
check the bounds properly
- range(len-1, -1, -1)
- The board was reverse, so be extra cautious of traversal
'''

class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        rows, cols =  len(board), len(board[0])
        
        dp  =  [float('inf')]*(rows*cols)
        dp[0] = 0
        
        for cell in range(1, 7):
            r = (cell)//rows
            c  = (cell)% rows
            
            if r%2==1:
                c =  - (c + 1)
                
            r = -(r+1)
                
            dp[cell] = 1
            
            if board[r][c] != -1:
                val = board[r][c]
                dp[val-1] = dp[cell] + 1
        
        for cell in range(7, rows*cols):
            r = (cell)//rows
            c  = (cell)% rows
            
            if r%2==1:
                c =  - (c + 1)
                
            r = -(r+1)
        
            dp[cell] = min( dp[cell-1], dp[cell-2], dp[cell-3], dp[cell-4], dp[cell-5], dp[cell-6]  ) + 1
            
            if board[r][c] != -1:
                val = board[r][c]
                dp[val-1] = dp[cell] + 1
                            
        print(dp)
        
    
    def printBoard(self, board: list[list[int]]) -> int:
        rows, cols =  len(board), len(board[0])
        
        dp  =  [ [float('inf')]*cols for _ in range(rows) ]
        # dp[-1][-1] = 0
        
        lr =  0
        start = 1
        
        for r in range(rows-1, -1,-1):
            if lr ==0:
                for c in range(cols):
                    dp[r][c] = start
                    start+=1
            else:
                for c in range(cols-1, -1, -1):
                    dp[r][c] = start
                    start+=1
                
            lr = lr^1
            
        print(dp)
        
        
# =======================================================
## LEETCODE OFFICIAL SOLUTION 
## lINK: https://leetcode.com/problems/snakes-and-ladders/solutions/2912646/snakes-and-ladders/

'''
Approach 1: Successful Approach, Breadth First Search
- Data Structures: deque --> ( enqueue, deque )
- Shortest path to reach the destination
- Total Number of edges --> answer (I think)
No of Test Cases Passed: All
'''

'''
NOTES: 
Boustrophedon style : Snake type traversal

#Mapping
```
columns = list(range(0, n))
for row in range(n - 1, -1, -1):
    for column in columns:
        cells[label] = (row, column)
        label += 1
    columns.reverse()
```

Time Complexity: O(n^2)
Space Complexity: O(n^2)

'''

from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        cells = [None] * (n**2 + 1)
        label = 1
        columns = list(range(0, n))
        for row in range(n - 1, -1, -1):
            for column in columns:
                cells[label] = (row, column)
                label += 1
            columns.reverse()
        dist = [-1] * (n * n + 1)
        q = deque([1])
        dist[1] = 0
        while q:
            curr = q.popleft()
            for next in range(curr + 1, min(curr + 6, n**2) + 1):
                row, column = cells[next]
                destination = (board[row][column] if board[row][column] != -1
                               else next)
                if dist[destination] == -1:
                    dist[destination] = dist[curr] + 1
                    q.append(destination)
        return dist[n * n]
        
 
 
# ====================================================
sol = Solution()

board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
res = sol.snakesAndLadders(board)
print(f"res={res}")
