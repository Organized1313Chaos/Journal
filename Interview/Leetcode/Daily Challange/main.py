import heapq
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        heap, ans, = [], [] 
        for s, e in intervals + [newInterval]: # add start & end to heap (-1 is start, 1 is end)
            heapq.heappush(heap, (s, -1))
            heapq.heappush(heap, (e, 1))
        cur, s = 0, None            
        while heap:                            
            i, val = heapq.heappop(heap)       # pop heap
            if s is None: s = i                # is s is None, assign i to s (interval start)
            cur += val                         # keep counting until close interval
            if not cur:                        # when cur == 0, meaning we can close the interval
                ans.append([s, i])             # append interval to ans
                s = None                       # reset s to None
        return ans        


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
        if not intervals: return [newInterval]
        N = len(intervals)
        start, end =newInterval
        
        index = 0
        
        
        for s, e in intervals:
            if start>e:
                index +=1
                continue
            break
        # print(index)
        try:
            min_ = min( start, intervals[index][0] )
        except:
            min_ = start

        index2 = N-1
        
        for i in range(N-1,index,-1):
            if end<intervals[i][0]:
                index2-=1
                continue
            break
        try:
            max_ = max( end, intervals[index2][1] )
        except:
            max_ = end
        # print(min_, max_)
        
        # Need to handle edge cases here
        if index==index2:
            if min_<intervals[index][0]:
                
                return intervals[:index] + [newInterval, intervals[index] ] + intervals[index2+1:]
            
        
        ans = intervals[:index] + [[min_,max_]] + intervals[index2+1:]
        return ans 
            
sol = Solution()
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
res = sol.insert(intervals, newInterval)
print(f"res={res}")

'''
p-m
a - o
r-s-k
e -i
'''
