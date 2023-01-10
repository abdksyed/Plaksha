# Lab Exercise - 4
# Priority Queues

import sys


class PriorityQueue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        # creating the list with indexing starting from 1 for simplicity
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    # minHeapify method to minHeapify the node at pos
    def minHeapify(self, pos):
        parent = (pos) // 2
        while self.Heap[pos] < self.Heap[parent]:
            self.Heap[pos], self.Heap[parent] = self.Heap[parent], self.Heap[pos]
            pos = parent
            parent = (pos) // 2

    def minHeapify_down(self):
        pos = 1
        while self.Heap[2 * pos] != 0:
            child = (
                2 * pos if self.Heap[2 * pos] < self.Heap[2 * pos + 1] else 2 * pos + 1
            )
            if self.Heap[pos] > self.Heap[child]:
                self.Heap[pos], self.Heap[child] = self.Heap[child], self.Heap[pos]
                pos = child
            else:
                break

    # Write this function to insert a node into the heap
    def insert(self, element):
        self.size += 1
        self.Heap[self.size] = element
        self.minHeapify(self.size)

    # Write this function to delete the rootNode
    def delete(self):
        popped_element = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.Heap[self.size] = 0
        self.size -= 1
        self.minHeapify_down()

        return popped_element

    # Write this function to return the rootNode (here the minimum element in PQ)
    def minimumElement(self):
        if self.isPqEmpty():
            return None
        return self.Heap[self.FRONT]

    # Write this function to return the size of the PriorityQueue
    def sizeOfPq(self):
        return self.size

    # Write this function to return if the priorityQueue is empty or not
    # Return boolean value
    def isPqEmpty(self):
        return not bool(self.size)

    # Function to print the contents of the heap
    def printPriorityQueue(self):
        for i in range(1, (self.size // 2) + 1):
            print(
                "Parent : "
                + str(self.Heap[i])
                + " Left Child : "
                + str(self.Heap[2 * i])
                + " Right Child : "
                + str(self.Heap[2 * i + 1])
            )

    # Function to build the PriorityQueue using minHeap
    def priorityQueue(self):
        for pos in range(self.size // 2, 0, -1):
            self.minHeapify(pos)
