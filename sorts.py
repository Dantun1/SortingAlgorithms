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
    test = 0
    while n >= 64:
        remainder |= n & 1
        test += remainder
        print(test)
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

# def pad_ascending_runs(sequence, min_run):
#     for i in range(0,len(sequence), min_run):
#         j = i
#         while j< (upper := min(i + min_run - 1, len(sequence) - 1)):
#             if sequence[j+1] < sequence[j]:
#                 insert_sort_subarray(sequence, i, upper)
#                 break
#             j+= 1


def reverse_subsequence(sequence, left, right):
    while left < right:
        sequence[left], sequence[right] = sequence[right], sequence[left]
        left += 1
        right -= 1


# def reverse_descending_runs(sequence):
#     i = 0
#     j = 0
#     while j < len(sequence)-1:
#         if sequence[j+1] > sequence[j] :
#             # print(i,sequence[i],j,sequence[j])
#             reverse_subsequence(sequence, i, j)
#             # print(sequence)
#             i = j+1
#         j+=1
#     reverse_subsequence(sequence, i, j)
#
#     return sequence

def find_and_prepare_runs(sequence, min_run):
    i = 0
    while i < len(sequence):
        run_start = i
        run_end = i + 1
        # The last element is trivially a non-descending run of length 1 so skip remaining logic in loop
        if run_end >= len(sequence):
            i+=1
            continue
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
        i = run_end + 1
    return sequence







runs = [random.randint(0,100) for _ in range(100)]
print(find_and_prepare_runs(runs, 32))

@timed_sort
def tim_sort(sequence):
    MIN_RUN = compute_min_run(len(sequence))

    find_and_prepare_runs(sequence, MIN_RUN)

    # for i in range(0, len(sequence), MIN_RUN):
    #
    #     insert_sort_subarray(sequence, i, min(i+MIN_RUN-1, len(sequence)-1))
    #
    #
    # size = MIN_RUN
    # while size < len(sequence):
    #     for start in range(0, len(sequence), 2*size):
    #         midpoint = start + size - 1
    #         end = min((start + 2*size - 1), (len(sequence)-1))
    #         merged_array = merge_sorted_sequences(
    #             sequence[start:midpoint+1],
    #             sequence[midpoint+1:end+1]
    #         )
    #         sequence[start:start+len(merged_array)] = merged_array
    #     size = 2*size

    return sequence
