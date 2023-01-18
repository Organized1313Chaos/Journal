# Heap Approach

# Link: https://leetcode.com/problems/insert-interval/solutions/845073/python-3-sweep-line-heap-explanations/

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


# ===============================================================================
def mergeIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        # if overlapping the update the end time
        #result end time >= start time
        if result[-1][1] >= intervals[i][0]:
            result[-1][1] = max(result[-1][1], intervals[i][1])
        else:
            result.append(intervals[i])
    return result

import random

intervals = []
start = 1
end = 10
for _ in range(4):
    
    num1 = random.randint(1,1000)
    num2 = random.randint(1,1000)
    
    if num1>num2:
        num1, num2 =  num2, num1
    
    new_ele = [num1,  num2]
    intervals.append(new_ele)
    
    start *=5
    end *= 10

print(intervals)
print(f"Initial Intervals-->\n{intervals}") 
result = mergeIntervals(intervals)
print(f"result-->\n{result}")
    
