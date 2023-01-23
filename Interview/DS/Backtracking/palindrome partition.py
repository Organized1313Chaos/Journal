'''
Link: https://leetcode.com/problems/palindrome-partitioning/

Solution: https://leetcode.com/problems/palindrome-partitioning/solutions/857510/palindrome-partitioning/
'''

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        N = len(s)

        def isPalindrome(string):
            if len(string)<2: return True
            l, r = 0, len(string)-1

            while l<r:
                if string[l]!= string[r]:
                    return False
                
                l+=1
                r-=1
            
            return True

        output = []

        def helper(start, path=[]):
            if start==N:
                output.append(path.copy())
                return 

            for index in range(start, N):
                if isPalindrome(s[start:index+1]):
                    path.append( s[start:index+1] )
                    helper(index + 1, path)
                    path.pop(-1)

        helper(0,[])

        return output

# ==============================================================

'''
Approach 2: 
Link: https://leetcode.com/problems/palindrome-partitioning/solutions/1667786/python-simple-recursion-detailed-explanation-easy-to-understand/
'''

from functools import lru_cache
class Solution(object):
    @lru_cache  # the memory trick can save some time
    def partition(self, s):
        if not s: return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in self.partition(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        return ans
    


'''
Time Complexity: O(n * 2^n)
- 2^n total substrings
- n ==> length of the substring

space-Complexity: O(n)
Max call stack is length of the string.
'''