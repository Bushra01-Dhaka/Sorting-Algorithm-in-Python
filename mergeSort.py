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

