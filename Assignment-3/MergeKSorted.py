
def merge_k_arrays(k, arrays):
    if not arrays:
        return None
    
    while len(arrays) > 1:
        merged = []
        for i in range(0, len(arrays), 2):
            list1 = arrays[i]
            if i+1 < len(arrays):
                list2 = arrays[i+1]
            else:
                list2 = None
        merged.append(merge_two(list1, list2))
        arrays = merged
    return arrays
            
def merge_two(list1, list2):
    merged = []
    while list1 and list2:
        if list1[0] < list2[0]:
            merged.append(list1[0])
            list1.pop(0)
        else:
            merged.append(list2[0])
            list2.pop(0)
    if list1:
        merged.append(list1)
    if list2:
        merged.append(list2)
    return merged
    




# print(merge_k_arrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))
print(merge_k_arrays(3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]
))