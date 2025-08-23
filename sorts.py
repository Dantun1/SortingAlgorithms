import math
import random
import time

def timed_sort(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
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

def compute_min_run(n):
    # divide n by 2 until we reach even groups between 32 and 64
    # track if any 1s are lost, add 1 to the min run if this is the case because otherwise a small group will remain. If too many 1s are lost, it doesnt work well
    #  99: 0110 0011 49: 0011 0001
    #  255: 1111 1111, r= 1 127: 0111 1111, 63:0011 1111 -> return 64 if return 63, then 255/63 leaves small remainder 3 group. 255/64 leaves large groups so less merging,
    remainder = 0
    while n >= 64:
        remainder |= n & 1
        n >>= 1
    return n + remainder


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

def reverse_subsequence(sequence, left, right):
    while left < right:
        sequence[left], sequence[right] = sequence[right], sequence[left]
        left += 1
        right -= 1


def find_next_run(sequence, run_start, min_run):

    run_end = run_start + 1
    # The last element is trivially a non-descending run of length 1 so skip remaining logic in loop
    if run_end >= len(sequence):
        return run_end
    # Check for descending run
    if sequence[run_end] < sequence[run_start]:
        # Find the end of the descending run and reverse
        while run_end < len(sequence) - 1 and sequence[run_end + 1] < sequence[run_end]:
            run_end += 1
        reverse_subsequence(sequence, run_start, run_end)
    else:
        while run_end < len(sequence) - 1 and sequence[run_end + 1] >= sequence[run_end]:
            run_end += 1

    # Pad runs shorter than min run
    run_length = run_end - run_start + 1
    if run_length < min_run:
        new_run_end = min(run_start + min_run - 1, len(sequence) - 1)
        insert_sort_subarray(sequence, run_start, new_run_end)
        run_end = new_run_end
    return run_end

def merge_sorted_inplace(sequence, start1, len1, start2, len2):
    # Writer to main sequence and pointer to temp list (always 0)
    ptr_insert = start1
    ptr_temp = 0
    # Copy shorter sequence into temp list, set start/end pointers to remaining main sequence portion
    if len1 <= len2:
        temp = sequence[start1:start1+len1]
        ptr_main = start2
        end_main = start2 + len2
    else:
        temp = sequence[start2:start2+len2]
        ptr_main = start1
        end_main = start1 + len1

    # Insert correct element
    while ptr_temp < len(temp) and ptr_main < end_main:
        if temp[ptr_temp] <= sequence[ptr_main]:
            sequence[ptr_insert] = temp[ptr_temp]
            ptr_temp += 1
        else:
            sequence[ptr_insert] = sequence[ptr_main]
            ptr_main += 1
        ptr_insert += 1

    # If main sequence list is depleted first, insert remaining from temp
    while ptr_temp < len(temp):
        sequence[ptr_insert] = temp[ptr_temp]
        ptr_insert += 1
        ptr_temp += 1

def merge_collapse(sequence, runs):
    # Maintain the timsort invariants on the runs stack by collapsing where necessary if at least 3 runs exist
    while len(runs) >= 3:
        startA, lenA = runs[-3]
        startB, lenB = runs[-2]
        startC, lenC = runs[-1]
        # Invariant 1, prevents smaller A run from being caught beneath large B+C by merging A and B if lenC > lenA
        if lenA <= lenB + lenC:
            if lenA < lenC:
                merge_sorted_inplace(sequence, startA, lenA, startB, lenB)
                runs.pop(-2)
                runs[-2] = (startA, lenA + lenB)
            else:
                merge_sorted_inplace(sequence, startB, lenB, startC, lenC)
                runs.pop()
                runs[-1] = (startB, lenB + lenC)
        # Invariant 2, ensures run sizes are strictly increasing deeper into the stack to setup balanced merges.
        elif lenB <= lenC:
            merge_sorted_inplace(sequence, startB, lenB, startC, lenC)
            runs.pop()
            runs[-1] = (startB, lenB + lenC)
        else:
            break

@timed_sort
def tim_sort(sequence):
    n = len(sequence)

    # Insertion sort if small
    if n < 64:
        return insertion_sort(sequence)

    MIN_RUN = compute_min_run(n)

    # Stack-like structure to store runs as they are found
    runs = []
    # Pointer to start of current run
    i = 0

    # Find, prepare and merge runs while iterating through sequence
    while i < n:
        run_end = find_next_run(sequence, i, MIN_RUN)
        runs.append((i, run_end - i + 1))
        # Enforce invariants when new run discovered for optimal/balanced merging
        merge_collapse(sequence, runs)

        i = run_end + 1

    # Merge remaining runs.
    while len(runs) > 1:
        start2, len2 = runs.pop()
        start1, len1 = runs.pop()
        merge_sorted_inplace(sequence, start1, len1, start2, len2)
        runs.append((start1, len1 + len2))

    return sequence

