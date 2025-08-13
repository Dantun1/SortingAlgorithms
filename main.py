from sorts import bubble_sort, insertion_sort, merge_sort, quick_sort
from random import randint


random_list = [i for i in range(500)]
# print(random_list)
bubble_sort(random_list[:])
insertion_sort(random_list[:])
merge_sort(random_list[:])
quick_sort(random_list[:])
# print(random_list)