
# ====================================================
# ====================================================
# ====================================================
'''
Leetcode Question
Date: January 20, 2023
Problem Number: 146
Name: LRU Cache 
'''
# ====================================================
# ====================================================
# ====================================================

'''
Approach 1: Successful Approach, Brute force 
- Take hasmap for cache memory
- 
No of Test Cases Passed: 100/100
'''

'''
NOTES:
pass

MISTAKES:
Initialised lst= [None]*capacity, and then I was appending,
            so None values were inserted into the hashmap
            
Don't forget the case when key is already in the cache,
so you have to update the pointers 
'''

# =======================================================

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.lst = []
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key]
            self.put( key, val )
            return val
        return -1


    def put(self, key: int, value: int) -> None:
        if len(self.cache) < self.capacity:

            if key in self.cache:
                self.lst.remove( key )
                del self.cache[key]

                self.cache[key] = value
                #Insert new element at the end
                self.lst.append(key)
                return

            self.cache[key] = value
            #Insert new element at the end
            self.lst.append(key)
            # self.Print()
            return
        
        if key in self.cache:
            self.lst.remove( key )
            del self.cache[key]

            self.cache[key] = value
            #Insert new element at the end
            self.lst.append(key)
            return

        # #pop the least used element
        old_key = self.lst.pop(0)

        if old_key in self.cache:
            del self.cache[old_key]
        self.cache[key] = value
        self.lst.append(key)
        
    def Print(self):
        print('='*10)
        print(f"lst  ==> { self.lst }")
        print(f"cache==> { self.cache }")
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# ===================================================================

s =  None

def execute_command(string, args):
    global s
    if string=="LRUCache":
        capacity = args[0]
        s =  LRUCache(capacity)
    
    elif string=="put":
        key, value = args[0], args[1]
        s.put(key, value)
        
    elif string=="get":
        key = args[0]
        s.get(key)
        
    s.Print()
        
# ===================================================================

commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
inputs = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

for cmd, args in zip(commands, inputs):
    execute_command(cmd, args)
        

#Testcase

# ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]

# [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
        
        
        

