import random
import math
import timeit
import matplotlib.pyplot as plt

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
    for _ in range(math.ceil(n * factor)):
        index1 = random.randint(0, n - 1)
        index2 = random.randint(0, n - 1)
        L[index1], L[index2] = L[index2], L[index1]
    return L


def dual_pivot_quicksort(L):
    if len(L) < 2:
        return L
    pivot1 = L[0]
    pivot2 = L[-1]
    left, center, right = [], [], []
    for num in L[1:len(L) - 1]:
        if num < min(pivot1, pivot2):
            left.append(num)
        elif num < max(pivot1, pivot2):
            center.append(num)
        else:
            right.append(num)
    return dual_pivot_quicksort(left) + [min(pivot1, pivot2)] + dual_pivot_quicksort(center) + [
        max(pivot1, pivot2)] + dual_pivot_quicksort(right)


def dual_pivot_quicksort(L):
    copy = quicksort_copy1(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy1(L):
    if len(L) < 2:
        return L
    left, right, center = [], [], []

    if L[0] < L[1]:
        pivot1 = L[0]
        pivot2 = L[1]
    else:
        pivot1 = L[1]
        pivot2 = L[0]

    for num in L[1:len(L) - 1]:
        if num <= pivot1:
            left.append(num)
        elif num < pivot2:
            center.append(num)
        else:
            right.append(num)
    return quicksort_copy1(left) + [pivot1] + quicksort_copy1(center) + [pivot2] + quicksort_copy1(right)


def tri_pivot_quicksort(L):
    copy = tri_pivot_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def tri_pivot_quicksort_copy(L):
    if len(L) < 3:
        return L
    pivot1 = L[0]
    pivot2 = L[1]
    pivot3 = L[2]
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

    for num in L[3:]:
        if num < min_val:
            quarter_1.append(num)
        elif num < center_val:
            quarter_2.append(num)
        elif num < max_val:
            quarter_3.append(num)
        else:
            quarter_4.append(num)
    return tri_pivot_quicksort_copy(quarter_1) + [min_val] + tri_pivot_quicksort_copy(
        quarter_2) + [center_val] + tri_pivot_quicksort_copy(quarter_3) + [max_val] + tri_pivot_quicksort_copy(quarter_4)


def quad_pivot_quicksort(L):
    copy = quad_pivot_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quad_pivot_quicksort_copy(L):
    if len(L) < 4:
        return L
    pivot1 = L[0]
    pivot2 = L[1]
    pivot3 = L[2]
    pivot4 = L[3]
    pivots = [pivot1, pivot2, pivot3, pivot4]
    pivots.sort()
    left_end, left_center, center, right_center, right_end = [], [], [], [], []

    min_val = min(pivots[0], pivots[1], pivots[2], pivots[3])
    max_val = 0
    center_val = 0
    if min_val == pivots[0]:
        center_val = min(pivots[1], pivots[2], pivots[3])
        if center_val == pivots[1]:
            center_val_2 = min(pivots[2], pivots[3])
            max_val = max(pivots[2], pivots[3])
        elif center_val == pivots[2]:
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

    for num in L[4:]:
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
    return quad_pivot_quicksort_copy(left_end) + [min_val] + quad_pivot_quicksort_copy(
        left_center) + [center_val] + quad_pivot_quicksort_copy(center) + [center_val_2] + quad_pivot_quicksort_copy(
        right_center) + [max_val] + quad_pivot_quicksort_copy(right_end)

x_axis = []
pivots = []
for i in range(100, 10001, 100):
    pivots.append(create_random_list(i))
    x_axis.append(i)

# # # Setup
y_axis = []
y_axis_dual = []
y_axis_tri = []
y_axis_quad = []

for i in pivots:
    x = i.copy()
    start = timeit.default_timer()
    my_quicksort(x)
    end = timeit.default_timer()
    y_axis.append(end - start)


for i in pivots:
    x = i.copy()
    start = timeit.default_timer()
    dual_pivot_quicksort(x)
    end = timeit.default_timer()
    y_axis_dual.append(end - start)

for i in pivots:
    x = i.copy()
    start = timeit.default_timer()
    tri_pivot_quicksort(x)
    end = timeit.default_timer()
    y_axis_tri.append(end - start)

for i in pivots:
    x = i.copy()
    start = timeit.default_timer()
    quad_pivot_quicksort(x)
    end = timeit.default_timer()
    y_axis_quad.append(end - start)


plt.scatter(x_axis, y_axis, label = "1_pivot")
plt.scatter(x_axis, y_axis_dual, label = "2_pivot")
plt.scatter(x_axis, y_axis_tri, label = "3_pivot")
plt.scatter(x_axis, y_axis_quad, label = "4_pivot")
plt.legend()
plt.show()

# def timetest_copy(runs, size):
#     total = 0
#     for _ in range(runs):
#         a = initialize_list(size)
#         b = []
#         # Times only when the copy method is called
#         start = timeit.default_timer()
#         b = a.copy()
#         end = timeit.default_timer()
#         # Total time
#         total += end - start
#     # Calculation for average times
#     return total/runs
#
# for i in range(100, 10000, 100):
#     print(i, timetest_copy(100, i))

#pivot = create_random_list(100000)

#print(pivot)
#tri_pivot_quicksort(pivot)
#print(pivot)

#############################################################################################

# PART 3 - WORST CASE PERFORMANCE

# Setup
# def setup_array(n):
#     x = create_random_list(n)
#     x.sort(reverse = True)
#     return worst_case
#
# x_axis = []
# y_axis = []
# y_axis_average = []
#
# # Worst case
# for i in range(500, 100001, 500):
#     a = setup_array(i)
#     x_axis.append(i)
#     start = timeit.default_timer()
#     quad_pivot_quicksort(a)
#     end = timeit.default_timer()
#     y_axis.append(end - start)
#
# pivots = []
# for i in range(500, 250001, 500):
#     pivots.append(create_random_list(i))
#     x_axis.append(i)
#
# for i in pivots:
#     x = i.copy()
#     start = timeit.default_timer()
#     quad_pivot_quicksort(x)
#     end = timeit.default_timer()
#     y_axis_average.append(end - start)
# plt.scatter(x_axis, y_axis, label = "Worst Case Performance")
# plt.scatter(x_axis, y_axis_average, label = "Average Case Performance")
# plt.legend()
# plt.show()
#


def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j + 1]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp


def insertion_sort(L):
    for i in range(len(L) - 1):
        insert_into(L, i)
        temp = L[i]
        L[i] = L[j]
        L[j] = temp


def insert_into(L, i):
    while i > 0:
        if L[i] < l[i - 1]:
            temp = L[i]
            L[i] = L[i - 1]
            L[i - 1] = temp
        else:
            return
        i -= 1


def selection_sort(L):
    for i in range(len(L) - 1):
        mindex = get_min_index(L, i)
        temp = L[i]
        L[i] = L[mindex]
        L[mindex] = temp


def get_min_index(L, n):
    mindex = n
    min_value = L[n]
    #
    for i in range(n, len(L)):
        if L[i] < L[mindex]:
            mindex = i
    return mindex