# bisect(list, num, beg, end)
# bisect_left(list, num, beg, end)
# bisect_right(list, num, beg, end) 

# list--> sorted

'''
Link--> https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
'''

import random 
import bisect

random.seed(10)

lst = [ random.randint(1,10) for _ in range(5)  ]
lst.sort()
print(lst)
    
# #bisect --> Inserts the leftmost index
# bisect, bisect_left, bisect_right


for _ in range(10):
    new_ele =  random.randint(1,10)
    print(new_ele)
    index = bisect.bisect(lst, new_ele)
    print(index)
    lst.insert(index, new_ele)
    print(lst)

# bisect Insort--> Inserts the element in sorted array
#insort_left, insort_right

for _ in range(10):
    new_ele =  random.randint(1,10)
    print(new_ele)
    bisect.insort(lst, new_ele)
    print(lst)

