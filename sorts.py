import random
import math


def my_quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)


def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1, n))
    return L


def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L


def dual_pivot_quicksort(L):
    if len(L) < 2:
        return L
    pivot1 = L[0]
    pivot2 = L[-1]
    left, center, right = [], [], []
    for num in L[1:len(L)-1]:
        if num < min(pivot1, pivot2):
            left.append(num)
        elif num < max(pivot1, pivot2):
            center.append(num)
        else:
            right.append(num)
    return dual_pivot_quicksort(left) + [min(pivot1, pivot2)] + dual_pivot_quicksort(center) + [max(pivot1, pivot2)] + dual_pivot_quicksort(right)


def dual_pivot_quicksor(L):
    copy = quicksort_copy1(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy1(L):
    if len(L) < 2:
        return L
    pivot1 = L[0]
    left, right, center = [], [], []
    pivot2 = L[len(L)-1]

    for num in L[1:len(L)-1]:
        if num < min(pivot1, pivot2):
            left.append(num)
        elif num < max(pivot1, pivot2):
            center.append(num)
        else:
            right.append(num)
    return quicksort_copy1(left) + [min(pivot1, pivot2)] + quicksort_copy1(center) + [max(pivot1, pivot2)] + quicksort_copy1(right)


def tri_pivot_quicksort(L):
    copy = tri_pivot_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def tri_pivot_quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot1 = L[0]
    pivot2 = L[len(L)-1]
    pivot3 = L[len(L)//2]
    pivots = [pivot1, pivot2, pivot3]
    pivots.sort()
    quarter_1, quarter_2, quarter_3, quarter_4 = [], [], [], []

    for num in L[1:len(L)-1]:
        if num < pivots[0]:
            quarter_1.append(num)
        elif num < pivots[1]:
            quarter_2.append(num)
        elif num < pivots[2]:
            quarter_3.append(num)
        else:
            quarter_4.append(num)
    return tri_pivot_quicksort_copy(quarter_1) + [pivots[0]] + tri_pivot_quicksort_copy(quarter_2) + [pivots[1]] + tri_pivot_quicksort_copy(quarter_3) + [pivots[2]] + tri_pivot_quicksort_copy(quarter_4)
    

def quad_pivot_quicksort(L):
    copy = quad_pivot_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quad_pivot_quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot1 = L[0]
    pivot2 = L[len(L)-1]
    pivot3 = L[(len(L)*3)//4]
    pivot4 = L[len(L)//4]
    pivots = [pivot1, pivot2, pivot3, pivot4]
    pivots.sort()
    left_end, left_center, center, right_center, right_end = [], [], [], [], []

    for num in L[1:len(L)-1]:
        if num < pivots[0]:
            left_end.append(num)
        elif num < pivots[1]:
            left_center.append(num)
        elif num < pivots[2]:
            center.append(num)
        elif num < pivots[3]:
            right_center.append(num)
        else:
            right_end.append(num)
    return quad_pivot_quicksort_copy(left_end) + [pivots[0]] + quad_pivot_quicksort_copy(left_center) + [pivots[1]] + quad_pivot_quicksort_copy(center) + [pivots[2]] + quad_pivot_quicksort_copy(right_center) + [pivots[3]] + quad_pivot_quicksort_copy(right_end)
    
    
    
    
