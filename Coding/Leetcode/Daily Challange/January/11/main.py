'''
Leetcode Question
Date: January 11, 2023
Problem Number: 1443 
Name: Minimum Time to Collect All Apples in a Tree
'''

'''
Approach 1:Successful, Inorder Traversal
'''

'''
NOTES:
1. Pass the parent as -1 initially
2. Construct a bidirectional graph, avoid back traversal using 
   parent==child: then continue

MISTAKES:
return type was hasApple, Didn't take account for if children has apple
'''

class Solution:
    def minTime(self, n: int, edges, hasApple) -> int:
        #During Backtrack if there is an apple in the path
        #Append positive count
        #otherwise append negative count
        
        #Can be startedfrom anywhere--> From root being an apple
        #From root not being an apple
        from collections import defaultdict
        tree = defaultdict(set)
        
        visited = set()
        
        for u,v in edges:
            if u in visited:
                tree[u].add(v)
                continue
            if v in visited:
                tree[v].add(u)                  
                continue
            tree[u].add(v)
            visited.add(u)
        
        tree = dict(tree)   
        result = 0
        
        def helper(node):
            nonlocal result
            
            print(node)
            if node not in tree: #leaf
                return hasApple[node]
            
            bool = False
            for i in tree[node]:
                result +=1
                if helper(i)==True:
                    bool = True
                    result+=1
                else:
                    result -=1
                
            return (bool or hasApple[node])
        
        helper(0)
            
        return result
               
sol = Solution()
n = 4
edges = [[0,2],[0,3],[1,2]]
hasApple = [False,True,False,False]
res = sol.minTime(n, edges, hasApple)
print(f"res={res}")
