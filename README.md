# Sorting Algorithm Performance Tracker

This project consists of Python implementations of some key sorting algorithms to help understand how each method works and compares performance-wise.

**Includes**: Bubble Sort, Insertion Sort, Merge Sort, Quick Sort, Tim Sort

## Overview

### Bubble Sort

Move largest element to end of sequence for up to N elements by comparing each element with up to N other elements.

`
Time Complexity: O(N^2)
`

>* Iterate through up to N elements for an N length list. 
>* During each iteration, move the largest element to the end of the array (hence, compare 1 less element per inner loop)
>* If no changes are made, is_sorted is left as True and we break out of the outer loop early



### Insertion Sort

Iterate through the list, keeping all elements preceding the current index in order (we start at index 1 so the single element sublist at sequence[0] is sorted by definition). 
Upon each iteration, ensure that the element of the current iteration is inserted into the correct position in the sublist,


` Time complexity: O(N^2)`

>* Starting from index i = 1, compare all preceding elements with sequence[i] to insert it into the correct location.
>* Working backwards from j = i-1, find index where sequence[i] belongs by copying all values at sequence[j] to sequence[j+1] if they are larger than sequence[i]
>* Insert sequence[i] either when j < 0 (no elements left to iterate) or when sequence[i] is less then sequence[j]


### Merge Sort

### Quick Sort

### Tim Sort

