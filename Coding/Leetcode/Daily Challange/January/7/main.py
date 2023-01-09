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
    def canCompleteCircuit(self, gas, cost) -> int:
        N = len(gas)
        
        for ind, val in enumerate( gas ):
            if ind==3:
                a =1
                pass            
            total = val
            flag = True
            for j in range(1, N+1):
                
                ind2 = (ind+j) % N
                total = total - cost[(ind2-1)%N] + gas[ind2] 
                
                if total<1:
                    flag = False
                    break 
                
            if flag==True:
                return ind
                
        
        return -1
            
            
sol = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
res = sol.canCompleteCircuit(gas, cost)
print(f"res={res}")
