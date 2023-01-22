
#python function to measure time taken of any given function

import random
import time

lst = [ random.randint(1, 10*8) for _ in range(10*8) ]

# Test 1
def timeFunc(func, lst):
    start = time.time()

    for case in lst:
        func(case)
        
    end = time.time()
    print(f"function name ==> {func.__name__}")
    print(f"total time taken ==> {end-start} seconds")

func1 = lambda x: x%2
func1.__name__ = "Simple modulo"
func2 = lambda x: x&1
func2.__name__ = "Using &1"

timeFunc( func1, lst )
timeFunc( func2, lst )