# ====================================================
'''
Leetcode Question
Date: January 28, 2023
Problem Number: 352 
Name: Data Stream as Disjoint Intervals
Link: https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
'''
# ====================================================

'''
Approach 1: Successful, Sorted Array Bisection Method
No of Test Cases Passed: All
'''

'''
NOTES:
- Language of question was little vague,

MISTAKES:
- Consider the last case, if l==N-1 then you have to append it in the output as well

Time Complexity: addnumber: O(log N), getInterval: O(N)
Space Complexity: O(N)
'''
# ====================================================


import bisect

class SummaryRanges:

    def __init__(self):
        self.arr =  [] 
        self.intervals = []

    def addNum(self, value: int) -> None:
        i = bisect.bisect_left(self.arr, value)
        if i != len(self.arr) and self.arr[i] == value:
            return
        self.arr.insert(i, value)
        
    def getIntervals(self) -> list[list[int]]:
        if not self.arr: return
            
        output = []
        l = 0
        N = len(self.arr)
        start = self.arr[0]
        
        for index in range(1,N):
            if (self.arr[index] - self.arr[l])==1:
                l +=1
                continue
            else:
                output.append( [start, self.arr[l]].copy() )
                l+=1
                start = self.arr[l]
                
        if l==N-1:
            output.append( [start, self.arr[l]] )

        self.intervals = output
    
    def Print(self):
        print(f"sorted array: {self.arr}")
        print(f"intervals: {self.intervals}")
        print('='*20)
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()

# ===================================================================

s =  None

def execute_command(string, args):
    global s
    if string=="SummaryRanges":
        print(f"Initialized Class:")
        s =  SummaryRanges()
    
    elif string=="addNum":
        num = args[0]
        print(f"add num={num}")
        s.addNum(num)
        
    elif string=="getIntervals":
        s.getIntervals()
        
        s.Print()
        
# ===================================================================

commands = ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
inputs = [[], [1], [], [3], [], [7], [], [2], [], [6], []]

for cmd, args in zip(commands, inputs):
    execute_command(cmd, args)
        