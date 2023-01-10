# Lab Exercise - 1

# Implementing Stacks using Arrays


class StackArrays:

    # Constructor for StackArrays class
    def __init__(self):
        self.array = []

    # Push: Add an element to the top of the stack
    def push(self, element):
        self.array.append(element)

    # Pop: Remove the topmost element in the stack and remove it
    def pop(self):
        if self.isEmpty():
            return
        return self.array.pop()

    # Returns the size of the stack
    def size(self):
        return len(self.array)

    # Return the element at the top of the stack without removing it
    def top(self):
        return self.array[-1]

    # Returns True is stack is empty, False if not
    def isEmpty(self):
        return self.size() is 0
