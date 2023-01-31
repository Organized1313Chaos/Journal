# ====================================================
'''
Leetcode Question
Date: January 31, 2023
Problem Number: 1626 
Name: Best Team With No Conflicts
Link: https://leetcode.com/problems/best-team-with-no-conflicts/description/
Official Solution Link: https://leetcode.com/problems/best-team-with-no-conflicts/solutions/?orderBy=most_votes 
'''
# ====================================================

'''
Approach 1: Failed Approach, Recursion and Memoization
Paradigm: Dynamic Programming
- Sort based on age the scores, append the index if necessary 
No of Test Cases Passed: 64/149
'''

'''
NOTES:
pass

MISTAKES:
- Understand the code properly

Time Complexity: O(N^2) (Mostly all the subsequencies?? Not sure) + O(Nlog(N)) [Sorting]
Space Complexity: O(N^2) (Memoization)
'''
# ====================================================
from functools import lru_cache
class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        lst = sorted(list(zip(ages, scores)), key= lambda x: (x[0], x[1]) )
        N = len(lst)

        @lru_cache
        def helper(prev, index):
            if index>=N:
                return 0

            #when there is no conflict
            if prev==-1 or lst[prev][1] <= lst[index][1]:
                # not Take it, take it
                return max( helper(prev, index+1) , lst[index][1]+ helper(index, index+1) )
            return helper(prev, index+1)

        answer = helper(-1, 0)

        return answer

# ====================================================
sol = Solution()
scores = [1,3,5,10,15]
ages = [1,2,3,4,5]
res = sol.bestTeamScore(scores, ages)
print(f"res={res}")

# =====================================================
# Solution 2
# Solution Link: https://leetcode.com/problems/best-team-with-no-conflicts/solutions/2886659/best-team-with-no-conflicts/

class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
                                                           
        dp = [0]*(1+max(ages))                         
                                                
        score_age = sorted(zip(scores, ages))
                                            
        for score, age in score_age:         
                                        
            dp[age] = score + max(dp[:age+1]) 
                                        
        return max(dp)                         
                                                                             
                                                 
        