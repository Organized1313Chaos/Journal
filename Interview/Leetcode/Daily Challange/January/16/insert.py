'''
Leetcode Question
Date: January 11, 2023
Problem Number: 57
Name: Insert Interval 
'''

'''
Approach 1: Partially Successful, redundent approach. 
No of Test Cases Passed: 146/156
'''

'''
NOTES:
pass

MISTAKES:
Reason Of Failure: Not able to cover the edge cases.
'''
class Solution:
    def insert(self, intervals, newInterval):
        result = []
        new_start,new_end = newInterval
        used = False

        for start, end in intervals:
            if end<new_start:
                result.append( [start, end] )
                continue
            if not used:
                min_ = min( new_start, start )
                max_ = max( new_end, end )
                result.append( [min_, max_] )
                used = True
                continue
            
            if result[-1][1]>end:
                continue
            
            if result[-1][1]<=start:
                result[-1][0] = min( result[-1][0], start )
                result[-1][1] = min( result[-1][1], end )
                continue
            
            if result[-1][1]<start:
                result.append( [start, end] )
                continue
            
            result.append( [start, end] )
            
        return result   
                
           
sol = Solution()
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
res = sol.insert(intervals, newInterval)
print(f"res={res}")
