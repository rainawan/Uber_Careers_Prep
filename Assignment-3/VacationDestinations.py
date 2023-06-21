"""
Raina Wan
06-17-2023

Vacation Destinations:
Given an origin city, a maximum travel time k, and pairs of destinations that can be reached directly 
from each other with corresponding travel times in hours, return the number of destinations within k 
hours of the origin. Assume that having a stopover in a city adds an hour of travel time.

Time Complexity: O(E*log(V^2)) => 
Space Complexity: 

Technique: 
BFS Graph Traversal

Time Spent:
40 minutes

Approach:

"""


from collections import defaultdict, deque

def vacation_destinations(cities, origin, k):
    travel_map = defaultdict(list)
    for start, end, dist in cities:
        travel_map[start].append((end, dist))
        travel_map[end].append((start, dist))

    q = deque([])
    q.append((origin, -1))
    visited = set()
    res = []

    while q:
        city, dist = q.popleft()
        if city in visited:
            continue
        visited.add(city)
        
        if dist != -1 and dist <= k:
            res.append(city)
        
        for neigh, distance in travel_map[city]:
            newDist = dist + distance + 1 # total distance + 1 hour travel time
            q.append((neigh, newDist))
    
    return (len(res), res)



if __name__ == "__main__":
    cities = [("Boston", "New York", 4), ("New York", "Philadelphia", 2), 
              ("Boston", "Newport", 1.5), ("Washington, D.C.", "Harper's Ferry", 1), 
              ("Boston", "Portland", 2.5), ("Philadelphia", "Washington, D.C.", 2.5)]

    print(vacation_destinations(cities,"New York", 5))
    # Number of destinations: 2
    # Destinations: ['Boston', 'Philadelphia']

    print(vacation_destinations(cities,"New York", 7))
    # Number of destinations: 4
    # Destinations: ['Boston', 'Philadelphia', 'Newport', 'Washington, D.C.']

    print(vacation_destinations(cities,"New York", 8))
    # Number of destinations: 6
    # Destinations: ['Boston', 'Philadelphia', 'Newport', 'Portland', 'Washington, D.C.', "Harper's Ferry"]