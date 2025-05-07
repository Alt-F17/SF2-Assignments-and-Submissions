def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

def mergeSort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = mergeSort(lst[:mid])
    right_half = mergeSort(lst[mid:])

    return merge(left_half, right_half)

lst = [38, 27, 43, 3, 9, 82, 10]
sorted_lst = mergeSort(lst)
print("Original list:", lst)
print("Sorted list:", sorted_lst)
