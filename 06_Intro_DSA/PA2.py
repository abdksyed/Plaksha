import sys
from collections import deque


class UnsortedPQ:
    def __init__(self):
        self.size = 0
        # creating the list with indexing starting from 1 for simplicity
        self.Heap = []

    # minHeapify method to minHeapify the node at pos
    def minHeapify(self, pos):
        pass

    # Write this function to insert a node into the heap
    def insert(self, element):
        self.size += 1
        self.Heap.append(element)

    # Write this function to delete the rootNode
    def delete(self):
        if self.isPqEmpty():
            return None
        min = 0
        for i in range(self.size):
            if self.Heap[i] < self.Heap[min]:
                min = i
        self.size -= 1
        return self.Heap.pop(min)

    # Write this function to return the rootNode (here the minimum element in PQ)
    def minimumElement(self):
        if self.isPqEmpty():
            return None
        min = 0
        for i in range(self.size):
            if self.Heap[i] < self.Heap[min]:
                min = i
        self.size -= 1
        return self.Heap[min]

    # Write this function to return the size of the PriorityQueue
    def sizeOfPq(self):
        return self.size

    # Write this function to return if the priorityQueue is empty or not
    # Return boolean value
    def isPqEmpty(self):
        return not bool(self.size)

    # Function to print the contents of the heap
    def printQueue(self):
        print(self.Heap)


class SortedPQ:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        # creating the list with indexing starting from 1 for simplicity
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.Front = 1

    # minHeapify method to minHeapify the node at pos
    def minHeapify(self, pos):
        pass

    # Write this function to insert a node into the heap
    def insert(self, element):
        pos = self.size
        while pos > 0:
            if self.Heap[pos] > element:
                self.Heap[pos + 1] = self.Heap[pos]
                pos -= 1
            else:
                break
        self.Heap[pos + 1] = element
        self.size += 1

    # Write this function to delete the rootNode
    def delete(self):
        if self.isPqEmpty():
            return None
        popped_element = self.Heap[self.Front]
        self.Heap[self.Front] = 0
        self.Front += 1

        return popped_element

    # Write this function to return the rootNode (here the minimum element in PQ)
    def minimumElement(self, withKey=False):
        if self.isPqEmpty():
            return None
        return self.Heap[self.Front]

    # Write this function to return the size of the PriorityQueue
    def sizeOfPq(self):
        return self.size - self.Front + 1

    # Write this function to return if the priorityQueue is empty or not
    # Return boolean value
    def isPqEmpty(self):
        return self.size < self.Front

    # Function to print the contents of the heap
    def printQueue(self):
        print(self.Heap)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class HeapPQ:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, value):
        if self.isPqEmpty():
            self.head = Node(value)
            self.size += 1
            return

        self.size += 1
        pathList = []
        i = self.size

        while i > 1:
            if i % 2 == 0:
                pathList.append("Left")
            else:
                pathList.append("Right")
            i //= 2
        # Reversing Path List, to traverse from
        # top to bottom
        pathList = pathList[::-1]

        node = self.head
        for ele in pathList[:-1]:
            if ele == "Left":
                node = node.left
            else:
                node = node.right

        new_node = Node(value)
        new_node.parent = node
        if pathList[-1] == "Left":
            node.left = new_node
        else:
            node.right = new_node

        self.minHeapifyUp(new_node)

    def delete(self):
        if self.isPqEmpty():
            return None
        elif self.size == 1:
            self.head = None
            self.size -= 1
            return

        pathList = []
        i = self.size

        while i > 1:
            if i % 2 == 0:
                pathList.append("Left")
            else:
                pathList.append("Right")
            i //= 2
        pathList = pathList[::-1]

        node = self.head
        for ele in pathList[:-1]:
            if ele == "Left":
                node = node.left
            else:
                node = node.right

        if pathList[-1] == "Left":
            self.head.value, node.left.value = node.left.value, self.head.value
            node.left.parent = None
            node.left = None
        else:
            self.head.value, node.right.value = node.right.value, self.head.value
            node.right.parent = None
            node.right = None

        self.size -= 1
        self.minHeapifyDown(self.head)

    def minHeapifyDown(self, node):
        if node.left == None and node.right == None:
            return
        elif node.right == None:
            if node.value > node.left.value:
                node.value, node.left.value = node.left.value, node.value
            # self.minHeapifyDown(node.left)
            return
        else:
            min_node = min([node, node.left, node.right], key=lambda x: x.value)
            if min_node == node:
                return
            node.value, min_node.value = min_node.value, node.value
            self.minHeapifyDown(min_node)

    def minHeapifyUp(self, node):
        while node != self.head:
            if node.value < node.parent.value:
                node.value, node.parent.value = node.parent.value, node.value
            else:
                break
            node = node.parent

    def peek(self):
        if self.isPqEmpty():
            return
        return self.head.value

    def sizeOfPq(self):
        return self.size

    def isPqEmpty(self):
        return not self.head

    def printQueue(self):
        if not self.head:
            return

        q = deque()
        q.append(self.head)
        while q:
            node = q.popleft()
            print(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
