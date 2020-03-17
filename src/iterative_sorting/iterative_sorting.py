# TODO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        temp_num = arr[cur_index]
        # TODO: find next smallest element
        # (hint, can do in 3 loc)
        for small_num in range(cur_index, len(arr)): 
            if temp_num >= arr[small_num]:
                temp_index = small_num
                temp_num = arr[small_num]
        # TODO: swap
        arr[temp_index] = arr[cur_index] 
        arr[cur_index] = temp_num
  
    return arr


# TODO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Boolean for while loop
    swapped = True

    # Looping as long as there has been one swap
    while swapped == True:
        # Counter to check for swaps
        count = 0
        for i in range(0, len(arr)-1):
            # Loop checks if the number at index is larger that the next
            if arr[i] > arr[i+1]:
                # Swaps number if condition is met
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # increments swap counter
                count += 1
        # If no swaps happen exit
        if count == 0:
            swapped = False

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # GET THE MAXIMUM NUMBER
    max_size = 0
    for i in range (0, len(arr)):
        if arr[i] > max_size:
            max_size = arr[i]

    count = [0] * (max_size + 1)

    # CHECK FOR NEGATIVES AND COUNT EVERY NUMBERS OCCURENCE
    for i in range(0, len(arr)):
        if float(arr[i]) > 0 or float(arr[i]) == 0:
            count[arr[i]] += 1
        else:
            return "Error, negative numbers not allowed in Count Sort"

    # GET THE RUNNING SUM
    for i in range(1, len(count)):
        count[i] += count[i - 1]


    new_array = [0] * len(arr)
    # MOVING IN REVERSE, PLACE THE NUMBERS INTO THE NEW ARRAY
    for i in range(len(arr)-1, -1, -1):
        # NUMBERS WILL ENTER THE NEW ARRAY AT POSITION -1 OF COUNT 
        new_array[count[arr[i]] - 1] = arr[i]
        # DECREMENT THE COUNT AFTER NUMBER IS ENTERED
        count[arr[i]] -= 1

    return new_array
