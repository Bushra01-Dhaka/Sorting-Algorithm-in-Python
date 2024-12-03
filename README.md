# Sorting-Algorithm-in-Python

##  Insertion Sort Algorithm

Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list. It is like sorting playing cards in your hands. You split the cards into two groups: the sorted cards and the unsorted cards. Then, you pick a card from the unsorted group and put it in the right place in the sorted group.

We start with second element of the array as first element in the array is assumed to be sorted.
Compare second element with the first element and check if the second element is smaller then swap them.
Move to the third element and compare it with the first two elements and put at its correct position
Repeat until the entire array is sorted.

``` python
# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]  # swap
            j -= 1

arr = [2,3,1,4,6,5]
insertion_sort(arr)
print("The sorted array: ", arr)

```

## Selection Sort Algorithm

Selection Sort is a comparison-based sorting algorithm. It sorts an array by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element. This process continues until the entire array is sorted.

First we find the smallest element and swap it with the first element. This way we get the smallest element at its correct position.
Then we find the smallest among remaining elements (or second smallest) and move it to its correct position by swapping.
We keep doing this until we get all elements moved to correct position.

``` python
# Selection Sort
def selection_sort(arr):
    for i in range(0,len(arr) - 1):
        cur_min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[cur_min_idx]:
                cur_min_idx = j
        arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]


arr = [2,6,5,1,3,4]
selection_sort(arr)
print("Sorted Array: ", arr)
```

## Merge Sort

Merge sort is a sorting algorithm that follows the divide-and-conquer approach. It works by recursively dividing the input array into smaller subarrays and sorting those subarrays then merging them back together to obtain the sorted array.

- Split the array in half
- Call Merge sort on each half to sort them recurcively
- Merge both sorted halves into one sorted array

``` python
def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        
        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = 0 # to keep track of the left most element of left_arr
        j = 0 # to keep track of the left most element of right_arr
        k = 0 # to keep track of the left most element of merge_arr
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # rest of the element that missed in array
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

test_arr = [2,6,5,1,7,4,3]
merge_sort(test_arr)
print("Sorted Array: ", test_arr)


```
