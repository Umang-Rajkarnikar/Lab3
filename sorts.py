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
    quarter_1, quarter_2, quarter_3, quarter_4 = [], [], [], []
   
    min_val = min(pivots[0], pivots[1], pivots[2])
    max_val = 0
    if min_val == pivots[0]:
        center_val = min(pivots[1], pivots[2])
        max_val = max(pivots[1], pivots[2])
    elif min_val == pivots[1]:
        center_val = min(pivots[0], pivots[2])
        max_val = max(pivots[0], pivots[2])
    else:
        center_val = min(pivots[0], pivots[1])
        max_val = max(pivots[0], pivots[1])

    
        
    max_val = max(pivots[0], pivots[1], pivots[3])
   
    list.remove() 

    for num in L[1:len(L)-1]:
        if num < min_val:
            quarter_1.append(num)
        elif num < center_val:
            quarter_2.append(num)
        elif num < max_val:
            quarter_3.append(num)
        else:
            quarter_4.append(num)
    return tri_pivot_quicksort_copy(quarter_1) + min_val + tri_pivot_quicksort_copy(quarter_2) + center_val + tri_pivot_quicksort_copy(quarter_3) + max_val + tri_pivot_quicksort_copy(quarter_4)
    

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
    
    min_val = min(pivots[0], pivots[1], pivots[2], pivot[3])
    max_val = 0
    center_val = 0
    if min_val == pivots[0]:
        center_val = min(pivots[1], pivots[2], pivots[3])
        if center_value == pivots[1]:
            center_val_2 = min(pivots[2], pivots[3])
            max_val = max(pivots[2], pivots[3])         
        elif center_value == pivots[2]:
            center_val_2 = min(pivots[1], pivots[3])
            max_val = max(pivots[1], pivots[3])                 
        else:
            center_val_2 = min(pivots[1], pivots[2])
            max_val = max(pivots[1], pivots[2])                 
    elif min_val == pivots[1]:
        center_val = min(pivots[0], pivots[2], pivots[3])
        if center_value == pivots[0]:
            center_val_2 = min(pivots[2], pivots[3])
            max_val = max(pivots[2], pivots[3])         
        elif center_value == pivots[2]:
            center_val_2 = min(pivots[0], pivots[3])
            max_val = max(pivots[0], pivots[3])                 
        else:
            center_val_2 = min(pivots[0], pivots[2])
            max_val = max(pivots[0], pivots[2])                 
    elif min_val == pivots[2]:
        center_val = min(pivots[0], pivots[1], pivots[3])
        if center_value == pivots[0]:
            center_val_2 = min(pivots[1], pivots[3])
            max_val = max(pivots[1], pivots[3])         
        elif center_value == pivots[1]:
            center_val_2 = min(pivots[0], pivots[3])
            max_val = max(pivots[0], pivots[3])                 
        else:
            center_val_2 = min(pivots[0], pivots[1])
            max_val = max(pivots[0], pivots[1])                 
    else:
        center_val = min(pivots[0], pivots[1], pivots[2])
        if center_value == pivots[0]:
            center_val_2 = min(pivots[1], pivots[2])
            max_val = max(pivots[1], pivots[2])         
        elif center_value == pivots[1]:
            center_val_2 = min(pivots[0], pivots[2])
            max_val = max(pivots[0], pivots[2])                 
        else:
            center_val_2 = min(pivots[0], pivots[1])
            max_val = max(pivots[0], pivots[1])              
            
    for num in L[1:len(L)-1]:
        if num < min_val:
            left_end.append(num)
        elif num < center_val:
            left_center.append(num)
        elif num < center_val_2:
            center.append(num)
        elif num < max_val:
            right_center.append(num)
        else:
            right_end.append(num)
    return quad_pivot_quicksort_copy(left_end) + min_val + quad_pivot_quicksort_copy(left_center) + center_val + quad_pivot_quicksort_copy(center) + center_val_2 + quad_pivot_quicksort_copy(right_center) + max_val + quad_pivot_quicksort_copy(right_end)
    
    
    
    
