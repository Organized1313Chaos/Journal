'''
Link: https://leetcode.com/problems/valid-palindrome/description/
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lookup = set('qwertyuiopasdfghjklzxcvbnm1234567890')
        s = s.lower()

        l, r = 0, len(s) -1 

        while l<r:
            if s[l] not in lookup:
                l+=1
                continue
            if s[r] not in lookup:
                r-=1
                continue
            
            if s[l]!=s[r]:
                return False

            l+=1
            r-=1

        return True


# Python 1-Liner
def isPalindrome(s):
    return s == s[::-1]