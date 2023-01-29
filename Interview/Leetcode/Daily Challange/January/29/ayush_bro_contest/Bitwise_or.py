# Problem State: 
# Given an array of bits of 2^n (formate 10000...)
# Take a subsequence, take or of those subsequences,
# if a0a4a5 is a sequence take or, a0|a4|a5 
# if the operation results in 101010101... 
# (flipped bits starting with 1)
# then delete the elements from the array and rerun the previous deletion operations

# Approach
# Or to be deleted: 10, 1000, 100000 (binary numbers with the multiplied by 4)
# create a counter of largest bits

#Testcases 
#Passed: All testcases, actual testcases were not tested
# Mode Of Exam: Hackerearth

def solve(nums):
    from collections import Counter

    cn = Counter(nums)

    # [1,2,4,8,..]
    lookup = [0]*36

    for num, freq in cn.items():
        count = 0
        while num!=0:
            num = num//2
            count+=1
        lookup[count-1] = freq

    index = 35
    while index>-1:
        if lookup[index]==0:
            index-=1
            continue
        
        val = lookup[index]
        j = index - 2
        lookup[index]= 0
        
        while j>-1:
            if lookup[j]<val:
                return "NO"
                #return 
            lookup[j] = lookup[j] - val
            j-=2

    return 'YES'

nums = [8,8,1,1,1,16,8,2,8,1]
print( solve(nums) )
        

    

