# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    # LOOP THROUGH MERGED ARRAY TO INSERT SORTED NUMBERS
    for i in range(0, len(merged_arr)):
        # CHECK IF FIRST ARRAY IS EMPTY 
        if len(arrA) == 0:
            merged_arr[i] = arrB[0]
            del arrB[0]
        # CHECK IF SECOND ARRAY IS EMPTY
        elif len(arrB) == 0:
            merged_arr[i] = arrA[0]
            del arrA[0]  
        # CHECK BETWEEN ARRAYS FOR WHICH NUMBER IS SMALLER       
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA[0]
            del arrA[0]
        else:
            merged_arr[i] = arrB[0]
            del arrB[0]

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # CHECK IF ARRAY HAS MORE THAN ONE ELEMENT INSIDE
    if len(arr) > 1:
        # SPLIT THE ARRAY
        split = len(arr) // 2
        first_half = arr[:split]
        second_half = arr[split:]

        # RECURSIVELY CONTINUE TO SPLIT THE ARRAY
        # MERGE ALL SPLIT ARRAYS BACK AS SORTED
        arr = merge(merge_sort(first_half), merge_sort(second_half))

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    left = arr[start:mid]
    right = arr[mid:end]

    for i in range(start, end):
        if len(left) == 0:
            arr[i] = right[0]
            del right[0]
        elif len(right) == 0:
            arr[i] = left[0]
            del left[0]
        elif left[0] < right[0]:
            arr[i] = left[0]
            del left[0]
        else:
            arr[i] = right[0]
            del right[0]

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    if len(arr) == 0:
        return arr

    if r - l > 1:
        middle = (l + r) // 2
        merge_sort_in_place(arr, l, middle)
        merge_sort_in_place(arr, middle, r)
        arr = merge_in_place(arr, l, middle, r)

    return arr
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort_in_place(arr1, 0, len(arr1)))


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
