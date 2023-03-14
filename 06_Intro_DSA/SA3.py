class HashTableChain:
    def __init__(self, size=50):
        self.size = size
        self.table = [None] * size
        self.CONSTANT = 42

    # hash function to determine the index for a given key
    def hasher(self, key):
        hash = key
        hash += self.CONSTANT * hash
        index = hash % self.size
        return index

    # insert a key-value pair to the hash table
    def insert(self, key):
        index = self.hasher(key)
        if not self.table[index]:
            self.table[index] = []
            self.table[index].append(key)
            return
        else:
            self.table[index].append(key)

    # retrieve the value for a given key
    def search(self, key):
        index = self.hasher(key)
        if not self.table[index]:
            return False  # Or should we return -1?
        for ele in self.table[index]:
            if ele == key:
                return True

    def delete(self, key):
        index = self.hasher(key)
        if not self.table[index]:
            return None
        for ele in self.table[index]:
            if ele == key:
                self.table.remove(ele)


def isSubset(arr1, arr2):
    obj = HashTableChain()
    for i in arr1:
        obj.insert(i)

    for i in arr2:
        if not obj.search(i):
            return False

    return True


class PriorityQueue:

    # Constructor
    def __init__(self, arr, size):
        # list of elements in the heap
        self.harr = arr
        self.capacity = None
        self.heap_size = size

        i = int((self.heap_size - 1) / 2)
        while i >= 0:
            self.minHeapify(i)
            i -= 1

    def parent(self, i):
        return (i - 1) / 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    # Returns minimum
    def getMin(self):
        return self.harr[0]

    # Method to remove minimum element (or root) from min heap
    def extractMin(self):
        if self.heap_size == 0:
            return float("inf")

        # Store the minimum value
        root = self.harr[0]

        # If there are more than 1 items, move the last item to root and call heapify
        if self.heap_size > 1:
            self.harr[0] = self.harr[self.heap_size - 1]
            self.minHeapify(0)
        self.heap_size -= 1
        return root

    # A method to heapify a subtree with root at given index.
    def minHeapify(self, i):
        if i < self.heap_size:
            leftC = self.left(i)
            rightC = self.right(i)
            if leftC < self.heap_size:
                leftChild = self.harr[leftC]
            else:
                leftChild = float("inf")
            if rightC < self.heap_size:
                rightChild = self.harr[rightC]
            else:
                rightChild = float("inf")
            if (
                (leftChild != float("inf"))
                and (leftChild < rightChild)
                and (leftChild < self.harr[i])
            ):
                self.harr[i], self.harr[leftC] = self.harr[leftC], self.harr[i]
                self.minHeapify(leftC)
            elif (
                rightChild != float("inf")
                and rightChild < leftChild
                and rightChild < self.harr[i]
            ):
                self.harr[i], self.harr[rightC] = self.harr[rightC], self.harr[i]
                self.minHeapify(rightC)


def kthLargest(arr, N, K):
    minHeap = PriorityQueue(arr, N)
    if (K > N) or (K <= 0):
        return None
    K = N - K + 1
    while K > 0:
        ans = minHeap.extractMin()
        K -= 1
    return ans
