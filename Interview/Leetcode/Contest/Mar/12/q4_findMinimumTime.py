# ====================================================
'''
Leetcode Contest Question
Date: March 13, 2023
Problem Number: 2589
Name: Minimum Time to Complete All Tasks
Link: https://leetcode.com/problems/minimum-time-to-complete-all-tasks/description/
Solution Link1 : https://leetcode.com/problems/minimum-time-to-complete-all-tasks/solutions/3287586/simple-diagram-explanation/
Solution Link2 : https://leetcode.com/problems/minimum-time-to-complete-all-tasks/solutions/3286676/python3-100-beats-easy-solution-greedy-sort-set/
 
'''
# ====================================================

'''
Approach 1: Successful Approach, Greedy Approach 
Paradigm: Hard, Greedy
No of Test Cases Passed: All
'''

'''
NOTES:
pass

MISTAKES:
- if duration<=0: break condition was outside of the loop
- It should be inside the loop with duration==0: break

Time Complexity: O(task_length*max(endtime))
Space Complexity: O(max(endtime))
'''
# ====================================================

class Solution:
    def findMinimumTime(self, tasks: list[list[int]]) -> int:
        tasks = sorted(tasks, key=lambda x: x[1])
        time_dict = set()
        for task in tasks:
            start, end, duration = task

            # reduce intersection time 
            for t in time_dict:
                if t>=start and t<=end:
                    duration-=1
                if duration==0:
                    break

            while end>0 and duration>0:
                if end not in time_dict:
                    duration -=1
                    time_dict.add(end)
                end -=1
        
        return len(time_dict)            