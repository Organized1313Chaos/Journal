# ====================================================
'''
Leetcode Question
Date: March 6, 2023
Problem Number: 50
Name: Pow(x, n)
Link: https://leetcode.com/problems/powx-n/
Solution Link: https://leetcode.com/problems/powx-n/solutions/1851860/simple-recursive-iterative-solutions/

Mathematical Solution: https://leetcode.com/problems/powx-n/solutions/749109/python-recursive-solution-faster-than-99/

Solution 3: https://leetcode.com/problems/powx-n/solutions/345741/python3-pow-x-n/
'''
# ====================================================

'''
Approach 1: Partially Successful Approach, Brute force 
Paradigm: 
- Simple loop execution
No of Test Cases Passed: 291/305
'''

'''
NOTES:
pass

Time Complexity: O(n) 
Space Complexity: O(1)
'''
# ====================================================

'''
Mistake 1: Forgot to include negative power cases
Mistake 2: In negative power case, take absolute value of it
Mistake 3: To check if number is odd or even we have to check a&1==1 and not a&2==1
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1

        if n>0:
            for i in range(n):
                res *= x
            
            return res
        
        for i in range(abs(n)):
            res = res/x
        
        return res
    
# =============================================
sol = Solution()
x = 2.00000
n = 10
res = sol.myPow(x, n)
print(f"res={res}")

# TestCase2
sol = Solution()
x = 2.00000
n = -2
res = sol.myPow(x, n)
print(f"res={res}")

# ===============================================
# Approach 2


'''
Approach 2: Partially Successful Approach, Recursion, Memoization
Paradigm: 
- Memoization
No of Test Cases Passed: 301/309
'''

'''
Mistake: x*x is not same as x**2
the later takes more computational power
'''

from functools import lru_cache
class Solution:
    def myPow(self, x: float, n: int) -> float:
        @lru_cache(maxsize=None)
        def helper(n):
            # Base Cases
            if n==0: 
                return 1
            if n==1: 
                return x
            if n==2: 
                return x*x        
        
            ans = helper(n//2)
            ans = ans*ans
            
            # odd power
            if abs(n)&1==1:
                ans = ans*x
            return ans
        
        ans = helper( abs(n))
        if n<0:
            return 1/ans
        return ans
        

# ======================================================
sol = Solution()
x = 2.00000
n = 10
res = sol.myPow(x, n)
print(f"res={res}")

# TestCase2
sol = Solution()
x = 2.00000
n = -2
res = sol.myPow(x, n)
print(f"res={res}")        

# Failed TestCase
x = 34.00515
n = -3
res = sol.myPow(x, n)
print(f"res={res}")        
            
# ========================================
'''
Solution Link: https://leetcode.com/problems/powx-n/solutions/1851860/simple-recursive-iterative-solutions/
'''
# Approach 3: iteration  
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif x in [0, 1] or n == 1:
            return x 
        else:
            pow = 1
            if n < 0:
                x = 1 / x
                n = -(n + 1)
                pow *= x

            while n > 0:
                if n % 2:
                    pow *= x
                    n -= 1
                else:
                    x *= x
                    n //= 2
            else:
                return pow            

# =============================================
sol = Solution()
x = 2.00000
n = 11
res = sol.myPow(x, n)
print(f"res={res}")
    

