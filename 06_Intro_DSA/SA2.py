from collections import deque

# Consecutive parent-child numbers in a binary tree


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    # Write this function to return the number of parent-child pairs
    # which are consecutive numbers
    def __init__(self):
        self.queue = deque()
        self.counter = 0

    # Comment out pass and write the code here
    def consecutiveNodes(self, A):
        if A is None:
            return self.counter
        if (A.left is None) and (A.right is None):
            return self.counter
        if A.left:
            self.counter += 1 if A.val == A.left.val - 1 else 0
            self.counter += 1 if A.val == A.left.val + 1 else 0
            self.queue.append(A.left)
        if A.right:
            self.counter += 1 if A.val == A.right.val - 1 else 0
            self.counter += 1 if A.val == A.right.val + 1 else 0
            self.queue.append(A.right)
        return self.consecutiveNodes(self.queue.popleft())


# Reverse Level Order Traversal


# class Node:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution2:
    def __init__(self):
        self.queue = deque()
        self.order = deque()

    # Comment out pass and write your code here
    def reverseLevelOrder(self, A):
        if A is None:
            return None
        if A.right:
            self.queue.append(A.right)
        if A.left:
            self.queue.append(A.left)
        self.order.appendleft(A.val)
        if len(self.queue) == 0:
            return list(self.order)
        return self.reverseLevelOrder(self.queue.popleft())
