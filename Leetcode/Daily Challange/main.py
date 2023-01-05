'''
Leetcode Daily Challange 
Date: January 5, 2023
Problem Number: 452
Name: Minimum Number of Arrows to Burst Balloons
'''

'''
Failed Approach 1: Merging Interval
Successful Approach 2: Interval Intersections
'''

class Solution:
    def findMinArrowShots(self, points) -> int:
        points = sorted(points)
        
        output = [points.pop(0)]
        points = list(reversed(points))
        
        while points:
            a0, b0 = output[-1][0], output[-1][1]
            a1, b1 = points.pop(-1)
            
            #(a1,a2) is a complete subset
            if (b1<=b0):
                output.pop(-1)
                output.append( [max(a0, a1), min(b0, b1)] )
                continue
            
            if (b1>b0 and a1<b0):
                output.pop(-1)
                output.append( [max(a0, a1), min(b0, b1)] )
                continue  
            
            #disjont
            if (a1>b0):
                 output.append( [a1, b1] )
                 continue
             
        return len(output)
 
sol = Solution()
points =  [[10,16],[2,8],[1,6],[7,12]]
res = sol.findMinArrowShots(points)
print(f"res={res}")
