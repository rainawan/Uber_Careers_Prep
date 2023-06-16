from collections import defaultdict

def vacation_destinations(cities, origin, k):
    travel_map = defaultdict(list)
    for start, end, dist in cities:
        travel_map[start].append((end, dist))
        travel_map[end].append((start, dist))

    res = 0

    def dfs(city, dist, num_cities):
        if city in visited:
            return 0
        if dist > k:
            return 0
        
        visited.add(city)
        num_cities += 1

        for neigh, distance in travel_map[city]:
            dfs(neigh, distance + dist, num_cities)
            return num_cities
        
        visited.remove(city)

    for neigh, distance in travel_map[origin]:
        visited = set()
        res += dfs(neigh, 0, res)
        print(visited)
    
    print(res)

    

if __name__ == "__main__":
    vacation_destinations([("Boston", "New York", 4), ("New York", "Philadelphia", 2), 
                        ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), 
                        ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)],
                        "New York", 5)