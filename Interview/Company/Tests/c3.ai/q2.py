#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMaxColors' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER money
#

def getMaxColors(prices, money):
    # Write your code here
    N = len(prices)
    l, r = 0, 0
    sm = 0
    output = 0
    
    while r < N and l<N:
     
        sm += prices[r]
        
        while l<N and sm > money:
            sm -= prices[l]
            l += 1
        
        output = max(r - l+1, output)
        r +=1

            
    return output
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    prices_count = int(input().strip())

    prices = []

    for _ in range(prices_count):
        prices_item = int(input().strip())
        prices.append(prices_item)

    money = int(input().strip())

    result = getMaxColors(prices, money)

    fptr.write(str(result) + '\n')

    fptr.close()
