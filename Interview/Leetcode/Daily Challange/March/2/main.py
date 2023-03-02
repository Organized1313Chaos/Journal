# ====================================================
'''
Leetcode Question
Date: March 2, 2023
Problem Number: 443
Name: String Compression
Link: https://leetcode.com/problems/string-compression/
Solution Link: https://leetcode.com/problems/string-compression/solutions/3245597/day-61-two-pointer-o-1-space-and-o-n-time-easiest-beginner-friendly-sol/
'''
# ====================================================

'''
Approach 1: Successful Approach, Brute force 
Paradigm: Simple Looping, Proper execution skills 
No of Test Cases Passed: All
'''

'''
NOTES:
pass

Mistakes: 
The question asked us to perform the operations in place 

Learning:
When you have to use index comparison use while instead of 
for loop

Time Complexity: O(N)
Space Complexity: O(N)
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
            res += [ chars[i-1]]

            for j in str(count):
                res.append(j)

            print(f"character: {chars[i-1]} & count: {count}")
            count  = 1

        if count!=1:
            res += [ chars[i] ]
            for j in str(count):
                res.append(j)
            
            output += 1 +  len(str(count))
        else:
            res += [ chars[i] ]
            output +=1

        
        print(f"character: {chars[i]} & count: {count}")
        for ind, val in enumerate(res):
            chars[ind] = val

        for j in range(ind, len(chars)-1):
            chars.pop(-1)
            

# ====================================================

sol = Solution()
chars = ["a","a","b","b","c","c","c"]
res = sol.compress(chars)
print(f"res={res}")


# =====================================================

class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        if n == 1:
            return 1
        
        i = 0
        j = 0
        
        while i < n:
            count = 1
            while i < n - 1 and chars[i] == chars[i+1]:
                count += 1
                i += 1
            
            chars[j] = chars[i]
            j += 1
            
            if count > 1:
                for c in str(count):
                    chars[j] = c
                    j += 1
            
            i += 1
        
        return j

        
