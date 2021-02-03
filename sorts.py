def partition(list, low, high):
    pivot = list[low]
    i = low+1
    j = high
    while True:
        while i <= j and list[j] >= pivot:
            j -= 1
        while i <= j and list[i] <= pivot:
            i += 1
        if i <= j:
            list[i], list[j] = list[j], list[i]
        else:
            break
    list[low], list[j] = list[j], list[low]
    return j

def quick_sort(list, low, high):
    if low < high:
        p = partition(list, low, high)
        quick_sort(list, low, p)
        quick_sort(list, p+1, high)
    return list
example = [10, 16, 8, 12, 15, 6, 3, 9, 5]
print(quick_sort(example, 0, 8))