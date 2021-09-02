def merge_sort(list_to_sort):
    if len(list_to_sort) == 1:
        return list_to_sort
    
    middle = len(list_to_sort) // 2
    
    left = merge_sort(list_to_sort[:middle])

    right = merge_sort(list_to_sort[middle:])

    return merge(left, right)

def merge(left, right):
    list_sorted = []

    while len(left) > 0 and len(right) > 0:
        if (left[0] < right[0]):
            list_sorted.append(left.pop(0))
        else:
            list_sorted.append(right.pop(0))
    
    while len(left) > 0:
        list_sorted.append(left.pop(0))
    
    while len(right) > 0:
        list_sorted.append(right.pop(0))

    return list_sorted
