from random import randrange

def bubble_sort(lst, comparison_function):
    swaps = 0
    sorted = False

    while not sorted:
        sorted = True
        for idx in range(len(lst) - 1):
            if comparison_function(lst[idx], lst[idx + 1]):
                sorted = False
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
                swaps += 1
    print("Bubble Sort: there were {} swaps".format(swaps))
    return lst

def quicksort(lst, start, end, comparison_function):
    if start >= end:
        return lst
    
    pivot_idx = randrange(start, end + 1)
    pivot_element = lst[pivot_idx]

    lst[end], lst[pivot_idx] = lst[pivot_idx], lst[end]

    less_than_pointer = start

    for i in range(start, end):
        if comparison_function(pivot_element, lst[i]):
            lst[i], lst[less_than_pointer] = lst[less_than_pointer], lst[i]
            less_than_pointer += 1
    lst[end], lst[less_than_pointer] = lst[less_than_pointer], lst[end]

    quicksort(lst, start, less_than_pointer - 1, comparison_function)
    quicksort(lst, less_than_pointer + 1, end, comparison_function)