# ====================================================
'''
Leetcode Question
Date: January 29, 2023
Problem Number: 460
Name: LFU Cache
Link: https://leetcode.com/problems/lfu-cache/description/
Solution Link: https://leetcode.com/problems/lfu-cache/solutions/2815229/lfu-cache/
'''
# ====================================================

'''
Approach 1: Successful Approach, Brute force 
Paradigm: Operating System, HashMap
- Maintain two HashMaps
1) key : (value, frequency)
2) frequency : list of keys
No of Test Cases Passed: All
'''

'''
NOTES:
- Leetcode iterates cases sequencially, 
meaning it does not run all cases and then 
returns the output
instead it runs a single input and then if
error occurs, or time constraints are violated

- LRU is maintained by LinkedList

MISTAKES:
- Every time you pop something,
- Or delete an element, make sure you also delete
- its list object within

Time Complexity: O(NLogN) for sorting frequency values, O(1) to get
Space Complexity: O(N)

# Correction
Instead of sorting to get minimum value,
u can initialize a minimum index value
to keep track of things
'''
# ====================================================

from collections import defaultdict
class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {} #key, (value,freq) pair
        self.frequency = defaultdict(list) #frequency, listvalue pair of keys
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            val, freq = self.cache[key]
            self.frequency[freq].remove(key)
            if not self.frequency[freq]:
                del self.frequency[freq]
            self.frequency[freq+1].append(key)
            
            #Mistake 1
            #update the original cache as well
            self.cache[key] = (val, freq+1)
            
            # print(f'get returns for key {key} --> {val}')
            self.Print()
            return val
        # print(f'get returns for key {key} --> {-1}')
        # self.Print()
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            val, freq = self.cache[key]
            self.frequency[freq].remove(key)
            self.frequency[freq+1].append(key)
            self.cache[key] = (value, freq+1)
            return 
        
        #if capacity is full
        #remove least frequently used key element
        if len(self.cache)==self.capacity:
            #track the least frequently used cache
            freq_arr = sorted(list(self.frequency.keys()))
            initial = 0
            f_remove = freq_arr[0]
            try:
                key_remove  = self.frequency[f_remove].pop(0) 
            except:
                del self.frequency[f_remove]
                self.put(key, value)
                return
                
            if not self.frequency[f_remove]:
                del self.frequency[f_remove]
            del self.cache[key_remove]
            
        #add the new entry
        self.cache[key] = (value, 1)
        self.frequency[1].append(key)
        
    
    def Print(self):
        return
        print(f"cache: ==> {dict(self.cache)}")
        print(f"Freq : ==> {dict(self.frequency)}")
        print("================================")
        
# ===================================================================

s =  None

def execute_command(string, args):
    global s
    if string=="LFUCache":
        capacity = args[0]
        print(f"Initialized Class:")
        print(f"Cache Capacity: {capacity}")
        s =  LFUCache(capacity)
        s.Print()
    
    elif string=="get":
        key = args[0]
        val = s.get(key)
        print(f"get key={key} ==> {val}")
        
    elif string=="put":
        key, value = args[0], args[1]
        s.put(key, value)
        
        s.Print()
        
# ===================================================================

commands = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
inputs = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

commands = ["LFUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]

inputs = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

for cmd, args in zip(commands, inputs):
    execute_command(cmd, args)