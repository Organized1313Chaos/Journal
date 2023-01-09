'''
Leetcode Question
Date: January 9, 2023
Problem Number: 239
Name: Sliding Window Maximum
'''

'''
Approach 1:Failed, Brute Force
'''

class Solution:
    def maxSlidingWindow(self, nums, k):
        # convert array to negative array to costruct a max_heap

        nums = [-i for i in nums ]

        import heapq

        res = []

        N = len(nums)

        heap = nums[:k].copy()
        heapq.heapify( heap )
        mx =  heap[0]
        res.append(-mx)
        
        for i in range(0,N-k):
            heap.remove(  nums[i]  )
            heap.append(  nums[i+k]  )
            heapq.heapify( heap )
            mx =  heap[0]
            res.append(-mx)
            
        return res
               
sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
res = sol.maxSlidingWindow(nums, k)
print(f"res={res}")
