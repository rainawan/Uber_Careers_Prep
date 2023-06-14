
class Heap:
    def __init__(self):
        self.arr = []
    
    def top(self):
        return self.arr[0]

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_index(self, index):
        return 2 * index + 1

    def get_right_index(self, index):
        return 2 * index + 2

    def swap(self, left, right):
        self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
    
    def insert(self, val):
        self.arr.append(val)
        parent = self.get_parent_index(len(self.arr) - 1)
        child = len(self.arr) - 1

        # keep swapping until child is less than parent
        while self.arr[child] < self.arr[parent]:
            self.swap(child, parent)
            child = parent
            parent = self.get_parent_index(len(self.arr) - 1)

    def remove(self):
        self.arr[-1], self.arr[0] = self.arr[0], self.arr[-1]
        curr = self.arr.pop(0)
        self.heapifyDown(0)
    
    def heapifyDown(self, val):
        root = val
        if self.arr[self.get_left_index(val)] < self.arr[root] and self.get_left_index(val) < len(self.arr):
            root = self.get_left_index(val)
        if self.arr[self.get_right_index(val)] < self.arr[root] and self.get_right_index(val) < len(self.arr):
            root = self.get_right_index
        if root != val:
            self.arr[root], self.arr[val] = self.arr[val], self.arr[root]
            self.heapifyDown(root)
        
    def print_heap(self):
        print(self.arr)
    

heap = Heap()
heap.insert(3)
heap.insert(5)
heap.insert(1)

heap.print_heap()

print(heap.top())
# Output: 1

heap.remove()
# print(heap.top())

