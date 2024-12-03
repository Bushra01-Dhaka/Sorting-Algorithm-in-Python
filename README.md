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
