def binary_search(arr, l, r, x):
    """Binary search algorithm.
    recursively search for x in arr[l:r]
    """    
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1

def bin_search(arr, l, r, x):
    """Binary search algorithm.
    iteratively search for x in arr[l:r]
    """
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return -1
