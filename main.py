from sorts import bubble_sort, insertion_sort, merge_sort, quick_sort, tim_sort
from random import randint



random_list = [randint(0,100) for i in range(10000)]
bubble_sort(random_list[:])
insertion_sort(random_list[:])
merge_sort(random_list[:])
quick_sort(random_list[:])
tim_sort(random_list[:])
