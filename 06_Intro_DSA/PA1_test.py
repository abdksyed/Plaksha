# PE1_test.py

# TEST CASES

import random
from time import process_time


def testStack(StackClass):
    stack = StackClass()
    stack.push(10)
    stack.push(20)

    assert stack.isEmpty() is False
    assert stack.pop() == 20

    assert stack.isEmpty() is False
    assert stack.pop() == 10

    assert stack.pop() is None

    for _ in range(100):
        stack.push(random.randint(0, 100))
    assert stack.size() == 100

    for _ in range(90):
        stack.pop()
    assert stack.size() == 10

    top_val = stack.top()
    assert stack.pop() == top_val

    print("Test Cases Passed")


def _convertLL2List(stack, list_data):

    stack.reverseList()

    reverse_list = []
    while stack.head is not None:
        reverse_list.append(stack.pop())
    reverse_list.reverse()

    return list(reversed(list_data)) == reverse_list


def testLinkedListStack(LinkedListStack):
    stack = LinkedListStack()

    list_data = []
    for _ in range(100):
        d = random.randint(0, 100)
        stack.push(d)
        list_data.append(d)

    assert _convertLL2List(stack, list_data)

    print("Linked List Specific Test Cases Passed")

    list_data = []
    stack = LinkedListStack()
    assert _convertLL2List(stack, list_data)

    list_data = ["APPLE"]
    stack = LinkedListStack()
    stack.push("APPLE")
    assert _convertLL2List(stack, list_data)


def testTime(stackClass, epochs=10_000, iterations=1500):
    stack = stackClass()
    timeList = []
    start = process_time()
    for _ in range(epochs):
        for _ in range(iterations):
            stack.push(random.randint(0, 100))
        end = process_time()
        timeList.append(end - start)
    return timeList
