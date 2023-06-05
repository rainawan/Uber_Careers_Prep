
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
