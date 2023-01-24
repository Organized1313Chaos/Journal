def network(counts):
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
    print(output_groups)
    
counts = [2,1,1,2,1]
network(counts)
