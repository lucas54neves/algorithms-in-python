def recursive_bubble_sort(list_to_sort, j):
    if j < 0:
        return list_to_sort
  
    for i in range(j):
        if list_to_sort[i] > list_to_sort[i + 1]:
            list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]

    return recursive_bubble_sort(list_to_sort, j - 1)

def bubble_sort(list_to_sort):
    for i in range(len(list_to_sort) - 1):
        for j in range(len(list_to_sort) - 1 - i):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]

    return list_to_sort