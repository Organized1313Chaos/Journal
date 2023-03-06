# ====================================================
'''
Leetcode Question
Date: March 6, 2023
Problem Number: 1539
Name: Kth Missing Positive Number
Link: https://leetcode.com/problems/kth-missing-positive-number/description/
Solution Link: 
'''
# ====================================================

'''
Approach 1: Successful Approach, Brute force using set 
Paradigm:  
No of Test Cases Passed: All
'''

'''
NOTES:
pass

MISTAKES:

Time Complexity: 
Space Complexity:
'''
# ====================================================
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        lookup = set(arr)

        start = 0
        i = 1
        while start<k:
            if i not in lookup:
                start +=1
            if start==k:
                return i
            i+=1
    
# ============================================================
sol = Solution()
arr = [2,3,4,7,11]
k = 5
res = sol.findKthPositive(arr, k)
print(f"res={res}")

# =============================================================
'''
CHAT-GPT Solution
'''

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        n = len(arr)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid
        return left + k

# ==============================================================================
'''
EXPLANATION:

The main function findKthPositive takes an array arr and an integer k as input, and returns the kth missing positive integer. The function uses binary search to find the index of the kth missing integer.

The variable n is the length of the array arr. The variables left and right are the left and right bounds of the binary search. The loop continues until left and right meet.

Inside the loop, the variable mid is the midpoint of the current search range. The expression arr[mid] - mid - 1 computes the number of missing integers between the first element of the array and the current element. If this value is less than k, we know that the kth missing integer is to the right of the current element, so we update left to mid + 1. Otherwise, we know that the kth missing integer is to the left of the current element, so we update right to mid.

After the loop, the variable left is the index where the kth missing integer would be if it were in the array. To get the actual value of the kth missing integer, we add k to left, which gives us the index of the kth missing integer in the extended sequence. The value of this integer is left + k.

'''
