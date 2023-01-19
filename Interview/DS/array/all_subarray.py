nums = [4,5,0,-2,-3,1]

N = len( nums )

for i in range(N):
    for j in range(i, N):
        print(nums[i:j+1])