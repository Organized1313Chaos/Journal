# ====================================================
'''
Leetcode Question
Date: March 8, 2023
Problem Number: 2187
Name: Minimum Time to Complete Trips
Link: https://leetcode.com/problems/minimum-time-to-complete-trips/
Solution Link: https://leetcode.com/problems/minimum-time-to-complete-trips/solutions/1802415/python3-java-c-binary-search-1-liner/
'''
# ====================================================

# Main Solution
'''
Paradigm: Binary Search
Note: If you are using heuristic to guess which value to choose, 
binary search is often the right solution
'''

class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        lo, hi = 1, totalTrips * min(time)

        def f(x):
            return sum(x // t for t in time) >= totalTrips
        
        while lo < hi:
            mid = (lo + hi) // 2
            if not f(mid): lo = mid + 1
            else: hi = mid
        return lo

# =========================================================================

'''
Approach 1: Failed Approach, Brute force 
Paradigm: Simple Execution using global time 
No of Test Cases Passed: 11/123
'''

'''
NOTES:
- Think first (It is the hardest part, leatn to do things in head.)

MISTAKES:
-

Time Complexity: 
Space Complexity:
'''
# ====================================================

class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        time = sorted(time)
        g_time = time[0]
        while totalTrips>0:
            i = 0
            while i<len(time) and totalTrips>0:
                a = time[i]
                # modfication 1:
                # global time is monotonically increasing
                if time[i]<=g_time and g_time%time[i]==0:
                    totalTrips -= 1
                else:
                    break
                i+=1
            if totalTrips<=0:
                return g_time
            g_time += time[0] 
        
    
# ==================================================================
sol = Solution()
time = [1,2,3]
totalTrips = 5
res = sol.minimumTime(time, totalTrips)
print(f"res={res}")

# ==================================================================
# Failed Test Case
time = [5,10,10]
totalTrips = 9
res = sol.minimumTime(time, totalTrips)
print(f"res={res}")

# ==================================================================


'''
Approach 1: Partial Successful Approach 
Paradigm: Looping 
No of Test Cases Passed: 62/123
'''

'''
NOTES:
- Think first (It is the hardest part, leatn to do things in head.)

MISTAKES:
-

Time Complexity: O(max(T)*Totaltrips)
Space Complexity:
'''
# =======================================================

class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        N = len(time)
        if N==1: return time[0]*totalTrips
        time = sorted(time)
        
        def helper(t):
            trip = 0
            for bus_time in time:
                if bus_time>t:
                    break
                trip += t//bus_time
            return trip
        i = 0
        last = i
        while True:
            res= helper(i)
            if res>=totalTrips:
                for j in range(last, i+1):
                    res= helper(j)
                    
                    if res>=totalTrips:
                        return j
                    # print(f"time-->{j}, total_trips-->{res}")
                return i
            # print(f"time-->{i}, total_trips-->{res}")
            last = i
            i+=time[0]
            
# ==================================================================
sol = Solution()
time = [1,2,3]
totalTrips = 5
res = sol.minimumTime(time, totalTrips)
print(f"res={res}")

# ==================================================================
# Failed Test Case
time = [5,10,12]
totalTrips = 9
res = sol.minimumTime(time, totalTrips)
print(f"res={res}")

# ===================================================================
'''
Failed Approach:
TestCases Passed: 35/123 cases passed
'''
class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        N = len(time)
        if N==1: return time[0]*totalTrips
        memo = {}
        def helper(t):
            trip = 0
            for bus_time in time:
                if bus_time>t:
                    break
                trip += t//bus_time
            return trip
        
        curr = N-1
        res = 0
        # Binary Trips
        while totalTrips>0:
            if curr in memo:
                trips = memo[curr]
            else:
                trips = helper(time[curr])
                memo[curr] = trips
                
            ##############################
            if trips>totalTrips:
                if curr==0:
                    totalTrips -= trips
                    res += time[curr]
                    continue
                curr = curr//2
                continue
            if trips==totalTrips:
                res += time[curr]
                return res
            
            if trips<totalTrips:
                totalTrips -= trips
                res += time[curr]
        
        return res
                
# Failed Test Case
sol = Solution()
# time = [5,10,10]
# totalTrips = 9

#Failed TestCases
time = [3,3,8]
totalTrips = 6

res = sol.minimumTime(time, totalTrips)
print(f"res={res}")

# =================================================================