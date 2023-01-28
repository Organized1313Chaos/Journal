# Code to merge consecutive numbers 
# into intervals 

arr = [1, 2, 3, 6, 7]

output = []
l = 0
N = len(arr)
start = arr[0]

for index in range(1,N):
    if (arr[index] - arr[l])==1:
        l +=1
        continue
    else:
        output.append( [start, arr[l]] )
        l+=1
        start = arr[l]

if l==N-1:
    output.append( [start, arr[l]] )
    
print(output)