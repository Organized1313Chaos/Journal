'''
Leetcode Daily Challange 
Date: January 6, 2023
Problem Number: 1833
Name: Maximum Ice Cream Bars
'''

'''
Successful Approach 1: Sort and pick minimum valued coin
'''
class Solution:
    def maxIceCream(self, costs, coins: int) -> int:
        costs = sorted(costs)
        count = 0
        for i in costs:
            coins -= i
            if coins<0:
                return count
            count+=1
            
        return count

sol = Solution()
costs = [1,3,2,4,1]
coins = 7
res = sol.maxIceCream(costs, coins)
print(f"res={res}")
