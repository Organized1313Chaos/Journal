#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'socialGraphs' function below.
#
# The function accepts INTEGER_ARRAY counts as parameter.
#

def socialGraphs(counts):
    # Write your code here
    from collections import defaultdict
    N = len(counts)
    graph = defaultdict(set)
    
    for index, value in enumerate(counts):
        graph[value].add(index)
        
    output_groups = []
    
    for key, val in graph.items():
        lst = list(val)
        lst.sort()
        
        for start in range(0 ,len(lst), key):
            output_groups.append( lst[start:start+key] )
    
    output_groups = sorted(output_groups , key= lambda x: x[0])
    
    for gp in output_groups:
        group_list = list(map(str, gp))
        group_string = " ".join(group_list)
        print(group_string)
if __name__ == '__main__':
    counts_count = int(input().strip())

    counts = []

    for _ in range(counts_count):
        counts_item = int(input().strip())
        counts.append(counts_item)

    socialGraphs(counts)
