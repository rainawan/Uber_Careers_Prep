from collections import defaultdict

def alternating_path(paths, origin, destination):
    graph = defaultdict(str)
    for i, j, color in paths:
        graph[(i, j)] = color
    
    visited = set()

    def dfs(start, end, color):
        print(start)
        if (start, end) in visited:
            return -1
        if not color:
            return -1

        visited.add((start, end))
        for key, val in graph:
            if end == key:
                dfs(start, end, not color)



    for key, val in graph:
        if key[0] == origin:
            dfs(key[0], key[1], True)



alternating_path([('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"), ('B', 'E', "blue"), ('C', 'B', "red"), ('D', 'C', "blue"), ('A', 'D', "red"), ('D', 'E', "red"), ('E', 'C', "red")], 
'A', 'E')




# graph = {
#     'A' : (['B', 'C'], 'blue')
# }

# print(graph['A'])
# for i in graph['A'][0]:
#     print(i)