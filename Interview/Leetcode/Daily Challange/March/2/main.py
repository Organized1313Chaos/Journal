print('hello')
print('bapu')



# ====================================================
'''
Leetcode Question
Date: January 11, 2023
Problem Number: 974
Name: Subarray Sums Divisible by K
Link: 
Solution Link: 
'''
# ====================================================

'''
Approach 1: Failed Approach, Brute force 
Paradigm: 
- Sort based on values, and append the index if necessary 
No of Test Cases Passed: 8/58
'''

'''
NOTES:
pass

MISTAKES:
if you append a copy of list (mutable objects)
Ensure that you store a copy instead of reference

Time Complexity: 
Space Complexity:
'''
# ====================================================
class Solution:
    def compress(self, chars: list[str]) -> int:
        if len(chars)==1: return 1
        res= []
        count = 1
        output = 0
        for i in range(1, len(chars)):
            if chars[i]==chars[i-1]:
                count+=1
                continue

            if count==1:
                res += [ chars[i-1] ]
                print(f"character: {chars[i-1]} & count: {1}")
                output += 1
                count =1
                continue
            
            output += 1 + len(str(count))
            res += [ chars[i-1], str(count) ]
            print(f"character: {chars[i-1]} & count: {count}")
            count  = 1

        if count!=1:
            res += [ chars[i], str(count) ]
            output += 1 +  len(str(count))
        else:
            res += [ chars[i] ]
            output +=1

        
        print(f"character: {chars[i]} & count: {count}")
        chars = res
            

# ====================================================

sol = Solution()
chars = ["a","a","b","b","c","c","c"]
res = sol.compress(chars)
print(f"res={res}")

        
