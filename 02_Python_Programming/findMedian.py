import random
import statistics
from typing import List


def compare(array: List, pivot: int):
    """
    Divide the Array into two parts based on pivot value

    Arguments:
        array: List - List of numbers
        pivot: int - The pivot value
    """
    right = []
    left = []
    for i in range(len(array)):
        if array[i] > pivot:
            right.append(array[i])
        elif array[i] < pivot:
            left.append(array[i])
    # Keeping Pivot element in Left Array
    left.append(pivot)

    return left, right


def findLesser(array: List, value: int):
    max = array[0]
    # Since last element is itself value, not checking it.
    for i in array[:-1]:
        if i > max and i <= value:
            max = i
    return max


def findMedian(array: List, k: int, isOdd: bool = True):
    """ """
    pivot = random.choice(array)
    left, right = compare(array, pivot)
    # Base Case
    if len(left) == k:
        if isOdd:
            return pivot
        # Failing when pivot itself is kth element during any iteration
        # As that element will get eleminated, so when it comes to k+1
        # element there is no kth element to search in findLesser.
        return (pivot + findLesser(left, pivot)) / 2

    if len(left) > k:
        return findMedian(left, k, isOdd)
    else:
        return findMedian(right, k - len(left), isOdd)


someArray = list(range(100))
random.shuffle(someArray)
k = len(someArray) // 2 + 1
isOdd = bool(len(someArray) % 2)
print(isOdd)
ans = findMedian(someArray, k, isOdd)

print(ans)
print(statistics.median(someArray))
