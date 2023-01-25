# ====================================================
'''
Leetcode Question
Date: January 21, 2023
Problem Number: 93
Name: Restore IP Addresses
Link: https://leetcode.com/problems/restore-ip-addresses/description/
Official Solution: https://leetcode.com/problems/restore-ip-addresses/solutions/2868540/restore-ip-addresses/
'''
# ====================================================

'''
Approach 1: Successful Approach, Backtracking

**Choose**: Choose the potential candidate substring of length 1,2,3
**Constraint**: 0 <= candidate <= 255, total dots = 4
**Goal**: reach end of the string with 4 dots
- 
No of Test Cases Passed: ALL
'''


'''
NOTES:
- Always append the copy of the path in backtraking
- Bound Constraints: min(idx+3, len(s))

MISTAKES:
- Do not forget leading zero cases

M digits, N different integers
Time Complexity: O(N * M^N)
Space Complexity: O(M*N)
'''
# ====================================================
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        output = []
        def helper(count, string, path):
            if string=="":
                return

            if count == 3:
                if string[0]=="0" and len(string)>1:
                    return

                if len(string)>3:
                    return 
                
                if 0<=int(string)<=255:
                    path = path + [string]
                    
                    output.append('.'.join(path) )
                
                return
               
            for i in range(1,4):
                if string[:i][0]=="0" and len(string[:i])>1:
                    break
                num = int(string[:i])
                if 0<=num<=255:
                    helper(count+1, string[i:], path +[string[:i]])
            
        helper(0, s, [])
        
        return output
    

# ======================================================
sol = Solution()
s =  "0000"
res = sol.restoreIpAddresses(s)
print(f"res={res}")