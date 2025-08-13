import math
import random
import time

def timed_sort(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken for {len(args[0])} elements with {func.__name__}  : {end - start}")
        return result
    return wrapper

# Bubble Sort
@timed_sort
def bubble_sort(sequence):
    for i in range(len(sequence)):
        sorted = True
        for j in range(len(sequence) - i -1):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
                sorted = False
        if sorted:
            break
    return sequence

# Insertion Sort

@timed_sort
def insertion_sort(sequence):
    for i in range(1, len(sequence)):
        val = sequence[i]
        j = i - 1
        while j >= 0 and  val < sequence[j]:
            sequence[j+1], sequence[j] = sequence[j], sequence[j+1]
            j -= 1

    return sequence

# Merge Sort
def merge_sorted_sequences(sequence1, sequence2):
    i,j = 0,0
    merged = []
    while i + j < len(sequence1) + len(sequence2):
        val1 = sequence1[i] if i<len(sequence1) else float(math.inf)
        val2 = sequence2[j] if j<len(sequence2) else float(math.inf)
        if val1 <= val2:
            merged.append(val1)
            i += 1
        else:
            merged.append(val2)
            j += 1
    return merged

def merge_sort_recursive(sequence):
    if len(sequence) == 1:
        return sequence
    mid = len(sequence) // 2
    left = merge_sort_recursive(sequence[:mid])
    right = merge_sort_recursive(sequence[mid:])

    return merge_sorted_sequences(left, right)

@timed_sort
def merge_sort(sequence):
    return merge_sort_recursive(sequence)

# Quick Sort
def quick_sort_recursive(sequence):
    if len(sequence) <= 1:
        return sequence
    pivot = random.choice(sequence)
    lt = [x for x in sequence if x < pivot]
    eq = [x for x in sequence if x == pivot]
    gt = [x for x in sequence if x > pivot]
    return quick_sort_recursive(lt) + eq + quick_sort_recursive(gt)


def partition(sequence, left, right):
    ...

@timed_sort
def quick_sort(sequence):
    return quick_sort_recursive(sequence)


# Tim Sort