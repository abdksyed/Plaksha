# Implementing Linked Lists

# Node class for the individual nodes
class Node:

    # constructor for Node class
    def __init__(self, data):
        self.data = data
        self.next = None


# Manager class to link the nodes and manage the overall list
class LinkedList:

    # constructor for LinkedList class
    def __init__(self):
        self.head = None

    # Push: Adds a new element at the head of the list
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    # Pop: Deletes the element at the last and returns the value of it
    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
        return popped

    # Returns the size of the linked list
    def size(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    # Function to insert a node containing data at some specified position between 1 and x
    def insert(self, data, position):
        # comment out pass and add your code here
        if position == 1 or self.isEmpty():
            self.push(data)
            return

        dummy = self.head
        # If postition is more than size, append at last
        position = min(position, self.size() + 1)

        count = 1
        while count < position - 1:
            count += 1
            dummy = dummy.next
        new_node = Node(data)
        new_node.next = dummy.next
        dummy.next = new_node

        return

    # Function to delete a node at the specified position between 1 and x
    def delete(self, position):
        # comment out pass and add your code here
        if self.isEmpty() or self.size() == 1:
            self.head = None
            return

        if position == 1:
            return self.pop()

        dummy = self.head
        # If postition is more than size, delete from last
        position = min(position, self.size())
        count = 1
        while count < position - 1:
            count += 1
            dummy = dummy.next

        deleted_value = dummy.next.data
        dummy.next = dummy.next.next

        return deleted_value

    # Return the element at the top of the linked list without removing it
    def top(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    # Return true is linked list is empty, False if not
    def isEmpty(self):
        return self.head is None

    def printIsEmpty(self):
        print("\Linked list is Empty\n") if self.isEmpty() else print(
            "\Linked list is not Empty\n"
        )

    # Reverses the linked list in place
    def reverseList(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def printList(self):
        temp = self.head
        print("The linked list created is as follows:")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Queue using an array

# Queue has FIFO order
class QueueUsingArrays:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = 0

    # Enqueue Function
    # Adding an element happens at the end of the list because it follows FIFO
    def enqueue(self, data, tag):
        # comment out pass and add your code here
        enum = list(range(self.size()))
        enum = enum[::-1]
        for idx, tup in zip(enum, self.queue[::-1]):
            if tup[1] == tag:
                self.queue = (
                    self.queue[: idx + 1] + [(data, tag)] + self.queue[idx + 1 :]
                )
                break
        # Doesn't Breal
        else:
            self.queue.append((data, tag))

        self.rear += 1

        return

    # Dequeue Function
    # Function to delete an element from the front of the queue
    def dequeue(self):
        if self.isEmpty():
            # print("\nQueue is empty")
            return None
        else:
            frontElement = self.queue[self.front]
            self.queue.pop(0)
            self.rear -= 1
            # print("Dequeued element is : ", frontElement)
            return frontElement

    # returns the size of the queue
    def size(self):
        return len(self.queue)

    # Function to check if the queue is empty or not
    def isEmpty(self):
        return True if len(self.queue) == 0 else False

    def printIsEmpty(self):
        print("Queue is Empty\n") if self.isEmpty() else print("Queue is not Empty\n")

    # Function to print all the queue elements
    def printQueue(self):
        if self.isEmpty():
            print("\nQueue is Empty")
        else:
            print(self.queue)

    # Print front of queue
    def frontElement(self):
        if self.isEmpty():
            return None
        else:
            return self.queue[self.front]
