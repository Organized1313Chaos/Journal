class MinHeap:
    def __init__(self, capacity):
        # Initialize the heap with a given capacity
        self.heap = [None] * capacity
        self.size = 0

    def parent(self, i):
        # Calculate the index of the parent node
        return (i - 1) // 2

    def left(self, i):
        # Calculate the index of the left child node
        return 2 * i + 1

    def right(self, i):
        # Calculate the index of the right child node
        return 2 * i + 2

    def heapify_down(self, i):
        # Maintain the min heap property by swapping values down the tree
        # Used for extraction of minimum element
        left = self.left(i)
        right = self.right(i)
        smallest = i

        if left < self.size and self.heap[left] < self.heap[i]:
            smallest = left

        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if i != smallest:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)

    def heapify_up(self, i):
        # Maintain the min heap property by swapping values up the tree
        # Used for insertion of new element
        
        parent = self.parent(i)
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = self.parent(i)

    def insert(self, value):
        # Insert a new value into the heap
        if self.size == len(self.heap):
            raise Exception("Heap is full")

        self.heap[self.size] = value
        self.heapify_up(self.size)
        self.size += 1

    def extract_min(self):
        # Extract the minimum value from the heap
        if self.size == 0:
            raise Exception("Heap is empty")

        min_value = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapify_down(0)

        return min_value

    def get_min(self):
        # Get the minimum value from the heap without removing it
        return self.heap[0]

    def get_size(self):
        # Get the number of values currently stored in the heap
        return self.size

    def is_empty(self):
        # Check if the heap is empty
        return self.size == 0
