# ====================================================
'''
Leetcode Question
Date: March 5, 2023
Problem Number: 2584
Name: Split the Array to Make Coprime Products
Link: https://leetcode.com/problems/split-the-array-to-make-coprime-products/description/
Solution Link: https://leetcode.com/problems/split-the-array-to-make-coprime-products/solutions/3258526/record-right-most-index-of-every-prime-factor-into-dictionary/
'''
# ====================================================

'''
Approach 1: Failed Approach, Brute force 
Paradigm: Using Counter, and using finding all the divisors
- 
No of Test Cases Passed: 31/39
'''

'''
NOTES:
pass

MISTAKES:
- To check GCD o two counters use &(intersections) instead of -(difference) operator
- got confused because of equivalent class

Time Complexity: O(max(n)*len(arr))
Space Complexity:
'''
# ====================================================



class Solution:
    def findValidSplit(self, nums: list[int]) -> int:
        lookup = {}
        
        import math
        from collections import Counter
        total_prod = Counter()
        for num in nums:
            temp =  self.prime_divisors(num)
            lookup[num] = temp
            total_prod += temp
        
        so_far = Counter()
        for index, num in enumerate(nums[:-1]):
            so_far = so_far + lookup[num]
            total_prod = total_prod - lookup[num]
            # print(f"so_far-->{so_far}, total_prod-->{total_prod}")
            # print(f"so_far_keys-->{set(so_far)}, total_prod_keys-->{set(total_prod)}\n")
            if not (set(so_far)&set(total_prod)):
                return index
            
        return -1
    
    # Tags: prime divisors, prime factors

    
    def prime_divisors(self, n):
        from collections import Counter
        from collections import defaultdict
        """
        Returns a list of prime divisors of n.
        """
        i = 2
        divisors = defaultdict(int)
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                divisors[i] += 1
        if n > 1:
            divisors[n] += 1
        return Counter(divisors)
