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
    
