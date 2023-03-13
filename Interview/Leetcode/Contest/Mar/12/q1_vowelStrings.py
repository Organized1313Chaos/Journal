# ====================================================
'''
Leetcode Contest Question
Date: March 13, 2023
Problem Number: 2586
Name: Count the Number of Vowel Strings in Range
Link: https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/description/
 
'''
# ====================================================

'''
Approach 1: Successful Approach, Simple execution
Paradigm: Easy, Greedy
No of Test Cases Passed: All
'''

'''
NOTES:
pass

MISTAKES:
N = len(words)
Time Complexity: O(O(N))
Space Complexity: O(1)
'''
# ====================================================
class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        words = words[left:right+1]
        vowels = 'aeiou'
        output = 0
        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                output +=1
                
        return output
            
        