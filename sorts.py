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
        is_sorted = True
        for j in range(len(sequence) - i -1):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
                is_sorted = False
        if is_sorted:
            break
    return sequence

# Insertion Sort

@timed_sort
def insertion_sort(sequence):
    for i in range(1, len(sequence)):
        val = sequence[i]
        j = i - 1
        while j >= 0 and  val < sequence[j]:
            sequence[j+1] = sequence[j]
            j -= 1
        sequence[j+1] = val

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
    if len(sequence) <= 1:
        return sequence
    mid = len(sequence) // 2
    left = merge_sort_recursive(sequence[:mid])
    right = merge_sort_recursive(sequence[mid:])

    return merge_sorted_sequences(left, right)

@timed_sort
def merge_sort(sequence):
    return merge_sort_recursive(sequence)

# Quick Sort (both not in place + in place)
def quick_sort_recursive(sequence):
    if len(sequence) <= 1:
        return sequence
    pivot = random.choice(sequence)
    lt = [x for x in sequence if x < pivot]
    eq = [x for x in sequence if x == pivot]
    gt = [x for x in sequence if x > pivot]
    return quick_sort_recursive(lt) + eq + quick_sort_recursive(gt)


def partition(sequence, left, right):
    pivot = sequence[right]
    i = left - 1
    for j in range(left, right):
        if sequence[j] <= pivot:
            i += 1
            sequence[i], sequence[j] = sequence[j], sequence[i]
    sequence[i+1], sequence[right] = sequence[right], sequence[i+1]
    return i+1

def quick_sort_inplace(sequence, left, right):
    if left<right:
        pivot = partition(sequence, left, right)
        quick_sort_inplace(sequence, left, pivot-1)
        quick_sort_inplace(sequence, pivot+1, right)

@timed_sort
def quick_sort(sequence):
    quick_sort_inplace(sequence, 0, len(sequence) - 1)
    return sequence

# Tim Sort

def insert_sort_subarray(sequence, left = 0, right = None):
    if right is None:
        right = len(sequence) - 1
    for i in range(left + 1, right + 1):
        val = sequence[i]
        j = i - 1
        while j >= left and val < sequence[j]:
            sequence[j+1]= sequence[j]
            j -= 1
        sequence[j+1] = val


@timed_sort
def tim_sort(sequence):
    MIN_RUN = 32

    for i in range(0, len(sequence), MIN_RUN):
        insert_sort_subarray(sequence, i, min(i+MIN_RUN-1, len(sequence)-1))

    size = MIN_RUN
    while size < len(sequence):
        for start in range(0, len(sequence), 2*size):
            midpoint = start + size - 1
            end = min((start + 2*size - 1), (len(sequence)-1))
            merged_array = merge_sorted_sequences(
                sequence[start:midpoint+1],
                sequence[midpoint+1:end+1]
            )
            sequence[start:start+len(merged_array)] = merged_array
        size = 2*size

    return sequence