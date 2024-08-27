def merge_sort(arr):
    """Sorts the given array using the merge sort algorithm.

    Args:
        arr: The array to be sorted.

    Returns:
        The sorted array.
    """

    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2  # find the middle index
    print("Mid: ", mid)
    left_half = arr[:mid] 
    print("A. Left Half: ", left_half)
    right_half = arr[mid:]
    print("A. Right Half: ", right_half)

    # Recursively sort each half
    left_half = merge_sort(left_half)
    print("B. Left Half: ", left_half)
    right_half = merge_sort(right_half)
    print("B. Right Half: ", right_half)

    print("Iteration Done...")
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left_half, right_half):
    """Merges two sorted arrays into a single sorted array.

    Args:
        left_half: The left half of the array.
        right_half: The right half of the array.

    Returns:
        The merged sorted array.
    """

    result = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        print("Merging...", left_half[i], right_half[j])
        if left_half[i] <= right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])  

            j += 1

    result.extend(left_half[i:])
    result.extend(right_half[j:])
    print("Merged Result So Far....", result)
    return result  

if __name__ == '__main__':
  # Example usage:
  arr = [3, 8, 1, 5, 9, 6, 4, 2, 7]
  sorted_arr = merge_sort(arr)
  print(sorted_arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]             