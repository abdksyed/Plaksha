import random
from typing import List


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


def partition(array: List, start, end):

    # Select some random Index to avoid worst case.
    pivot_location = random.randint(start, end - 1)

    # Swap that random element with start element
    swap(array, start, pivot_location)  # Inplace Array Swap

    # Now pivot element is on start index
    pivot_location = start

    swap_location = start + 1
    for i in range(start, end + 1):
        if array[i] < array[pivot_location]:
            swap(array, swap_location, i)
            swap_location += 1
    swap(array, swap_location - 1, start)

    return start, swap_location - 1, end


def quickSort(array, start, end):
    if start >= end:
        return

    start, mid, end = partition(array, start, end)
    quickSort(array, start, mid - 1)
    quickSort(array, mid + 1, end)

    return array


someArray = list(range(1000))
random.shuffle(someArray)
assert sorted(someArray) == quickSort(someArray, 0, len(someArray) - 1)

randomArray = random.choices(list(range(1000)), k=1000)
assert sorted(randomArray) == quickSort(randomArray, 0, len(randomArray) - 1)


stringArray = [
    "banana",
    "catapult",
    "home",
    "fish",
    "donkey",
    "elephant",
    "grandiose",
    "apple",
]
assert sorted(stringArray) == quickSort(stringArray, 0, len(stringArray) - 1)
