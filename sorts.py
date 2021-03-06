import random
import math
import timeit
import matplotlib.pyplot as plt

def partition(lists, low, high):
    pivot = lists[low]
    i = low+1
    j = high
    while True:
        while i <= j and lists[j] >= pivot:
            j -= 1
        while i <= j and lists[i] <= pivot:
            i += 1
        if i <= j:
            lists[i], lists[j] = lists[j], lists[i]
        else:
            break
    lists[low], lists[j] = lists[j], lists[low]
    return j


def quicksort_inplace_copy(lists, low, high):
    if low < high:
        p = partition(lists, low, high)
        quicksort_inplace_copy(lists, low, p)
        quicksort_inplace_copy(lists, p+1, high)
    return lists


def quicksort_inplace(lists):
    return quicksort_inplace_copy(lists, 0, len(lists)-1)


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
    copy = dual_pivot_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def dual_pivot_quicksort_copy(L):
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
    return dual_pivot_quicksort_copy(left) + [pivot1] + dual_pivot_quicksort_copy(center) + [pivot2] + dual_pivot_quicksort_copy(right)


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
################################################################################################################
# OPTIMIZED LIST

def quad_pivot_quicksort_opt(L):
    copy = quad_pivot_quicksort_opt_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quad_pivot_quicksort_opt_copy(L):
    if len(L) < 4:
        return L
    pivot1 = L[0]
    pivot2 = L[1]
    pivot3 = L[2]
    pivot4 = L[3]
    pivots = [pivot1, pivot2, pivot3, pivot4]
    pivots.sort()
    left_end, left_center, center, right_center, right_end = [], [], [], [], []

    index = 0
    for i in range(len(L)-1):
        if L[i] < L[i + 1]:
            temp = pivots[index]
            pivots[index] = L[i]
            L[i] = temp
            index+=1
            if index == 4:
                break


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
        if center_val == pivots[0]:
            center_val_2 = min(pivots[2], pivots[3])
            max_val = max(pivots[2], pivots[3])
        elif center_val == pivots[2]:
            center_val_2 = min(pivots[0], pivots[3])
            max_val = max(pivots[0], pivots[3])
        else:
            center_val_2 = min(pivots[0], pivots[2])
            max_val = max(pivots[0], pivots[2])
    elif min_val == pivots[2]:
        center_val = min(pivots[0], pivots[1], pivots[3])
        if center_val == pivots[0]:
            center_val_2 = min(pivots[1], pivots[3])
            max_val = max(pivots[1], pivots[3])
        elif center_val == pivots[1]:
            center_val_2 = min(pivots[0], pivots[3])
            max_val = max(pivots[0], pivots[3])
        else:
            center_val_2 = min(pivots[0], pivots[1])
            max_val = max(pivots[0], pivots[1])
    else:
        center_val = min(pivots[0], pivots[1], pivots[2])
        if center_val == pivots[0]:
            center_val_2 = min(pivots[1], pivots[2])
            max_val = max(pivots[1], pivots[2])
        elif center_val == pivots[1]:
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
    return quad_pivot_quicksort_opt_copy(left_end) + [min_val] + quad_pivot_quicksort_opt_copy(
        left_center) + [center_val] + quad_pivot_quicksort_copy(center) + [center_val_2] + quad_pivot_quicksort_copy(
        right_center) + [max_val] + quad_pivot_quicksort_copy(right_end)
################################################################################################################

# IN-PLACE


def test(x):

    total = 0

    for i in range(10):
        start = timeit.default_timer()
        my_quicksort(x)
        end = timeit.default_timer()
        total+=end-start
    return total/10

def in_place_test():
    x_axis = []
    pivots = []
    for i in range(100, 1001, 100):
        pivots.append(create_random_list(i))
        x_axis.append(i)

    # Setup
    y_axis = []
    y_axis_inplace = []

    for i in pivots:
        x = i.copy()
        y_axis.append(test(x))


    for i in pivots:
        x = i.copy()
        y_axis_inplace.append(test(x))

    plt.scatter(x_axis, y_axis, label="Quicksort")
    plt.scatter(x_axis, y_axis_inplace, label="In-Place Quicksort")
    plt.title("Quicksort vs. Inplace Quicksort vs. List Size (n)")
    plt.xlabel("List Size (n)")
    plt.ylabel("Runtime")
    plt.legend()
    plt.show()


################################################################################################################

# MULTI-PIVOT

def multi_pivot():
    x_axis = []
    pivots = []
    for i in range(100, 10001, 100):
        pivots.append(create_random_list(i))
        x_axis.append(i)

    # # Setup
    y_axis = []
    y_axis_dual = []
    y_axis_tri = []
    y_axis_quad = []
    y_final = []

    for i in pivots:
        x = i.copy()
        start = timeit.default_timer()
        final_sort(x)
        end = timeit.default_timer()
        y_final.append(end - start)


    # for i in pivots:
    #     x = i.copy()
    #     start = timeit.default_timer()
    #     my_quicksort(x)
    #     end = timeit.default_timer()
    #     y_axis.append(end - start)


    # for i in pivots:
    #     x = i.copy()
    #     start = timeit.default_timer()
    #     dual_pivot_quicksort(x)
    #     end = timeit.default_timer()
    #     y_axis_dual.append(end - start)

    # for i in pivots:
    #     x = i.copy()
    #     start = timeit.default_timer()
    #     tri_pivot_quicksort(x)
    #     end = timeit.default_timer()
    #     y_axis_tri.append(end - start)

    for i in pivots:
        x = i.copy()
        start = timeit.default_timer()
        quad_pivot_quicksort(x)
        end = timeit.default_timer()
        y_axis_quad.append(end - start)

   # plt.scatter(x_axis, y_axis, label="1_pivot")
   # plt.scatter(x_axis, y_axis_dual, label="2_pivot")
   # plt.scatter(x_axis, y_axis_tri, label="3_pivot")
    plt.scatter(x_axis, y_axis_quad, label="4_pivot")
    plt.scatter(x_axis, y_final, label="final")
    plt.title("Quicksort vs. Multi-Pivot Quicksort vs. List Size (n)")
    plt.xlabel("List Size (n)")
    plt.ylabel("Runtime")
    plt.legend()
    plt.show()

#############################################################################################

# PART 3 - WORST CASE PERFORMANCE

# Setup


def setup_array(n):
    x = create_random_list(n)
    x.sort(reverse=True)
    return x


def worst_case_test():
    x_axis = []
    y_axis = []

    # Worst case
    for i in range(10, 2500, 10):
        a = setup_array(i)
        x_axis.append(i)
        start = timeit.default_timer()
        quad_pivot_quicksort(a)
        end = timeit.default_timer()
        y_axis.append(end - start)

    plt.scatter(x_axis, y_axis)
    plt.title("Worst Case Performance vs. List Size (n)")
    plt.xlabel("List Size (n)")
    plt.ylabel("Runtime")
    plt.show()

##############################################################################

# FACTOR


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
    return L


def insert_into(L, i):
    while i > 0:
        if L[i] < L[i - 1]:
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


def factor_test():
    factor_list = []
    x_axis_factor = []
    y_quick = []
    y_bubble = []
    y_insertion = []
    y_selection = []

    for i in range(1, 100):
         factor_list.append(create_near_sorted_list(1000, i/1000))
         x_axis_factor.append(i/1000)

    for i in factor_list:
        x = i.copy()
        start = timeit.default_timer()
        quad_pivot_quicksort(x)
        end = timeit.default_timer()
        y_quick.append(end - start)

    for i in factor_list:
        x = i.copy()
        start = timeit.default_timer()
        bubble_sort(x)
        end = timeit.default_timer()
        y_bubble.append(end - start)

    for i in factor_list:
        x = i.copy()
        start = timeit.default_timer()
        selection_sort(x)
        end = timeit.default_timer()
        y_selection.append(end - start)

    for i in factor_list:
        x = i.copy()
        start = timeit.default_timer()
        insertion_sort(x)
        end = timeit.default_timer()
        y_insertion.append(end - start)

    plt.scatter(x_axis_factor, y_quick, label="Quick sort - Quad pivot")
    plt.scatter(x_axis_factor, y_bubble, label="Bubble sort")
    plt.scatter(x_axis_factor, y_selection, label="Selection sort")
    plt.scatter(x_axis_factor, y_insertion, label="Insertion sort")
    plt.title("Quicksort vs. Elementary Sorts vs. Near-Sorted Factor")
    plt.xlabel("Near-Sorted Factor")
    plt.ylabel("Runtime")
    plt.legend()
    plt.show()

###############################################################################################################

# SMALL LISTS

def small_list_test(n):
    factor_list = []
    x_axis_factor = []
    y_quick = []
    y_bubble = []
    y_insertion = []
    y_selection = []

    for i in range(5, n, 1):
         factor_list.append(create_random_list(i))
         x_axis_factor.append(i)

    for i in factor_list:
        x = i.copy()
        start = timeit.default_timer()
        quad_pivot_quicksort(x)
        end = timeit.default_timer()
        y_quick.append(end - start)

    for i in factor_list:
        x = i.copy()
        start = timeit.default_timer()
        bubble_sort(x)
        end = timeit.default_timer()
        y_bubble.append(end - start)

    for i in factor_list:
        x = i.copy()
        start = timeit.default_timer()
        selection_sort(x)
        end = timeit.default_timer()
        y_selection.append(end - start)

    for i in factor_list:
        x = i.copy()
        start = timeit.default_timer()
        insertion_sort(x)
        end = timeit.default_timer()
        y_insertion.append(end - start)

    if n <= 30:

        plt.scatter(x_axis_factor, y_quick, label = "Quick sort - Quad pivot")
        plt.scatter(x_axis_factor, y_selection, label = "Selection sort")
        plt.scatter(x_axis_factor, y_insertion, label = "Insertion sort")
        plt.title("Quicksort vs. Insertion Sort vs. List Size (n)")
        plt.xlabel("List Size (n)")
        plt.ylabel("Runtime")
        plt.legend()
        plt.show()
    else:
        plt.scatter(x_axis_factor, y_quick, label = "Quick sort - Quad pivot")
        plt.scatter(x_axis_factor, y_bubble, label = "Bubble sort")
        plt.scatter(x_axis_factor, y_selection, label = "Selection sort")
        plt.scatter(x_axis_factor, y_insertion, label = "Insertion sort")
        plt.title("Quicksort vs. Insertion Sort vs. Selection Sort vs. List Size (n)")
        plt.xlabel("List Size (n)")
        plt.ylabel("Runtime")
        plt.legend()
        plt.show()
    

 ####################################################################################
 # FinalSort
def final_sort(L):
    copy = final_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def final_copy(L):
    if len(L) < 4:
        return L

    if len(L) < 10:
        return insertion_sort(L)

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
    return final_copy(left_end) + [min_val] + final_copy(
        left_center) + [center_val] + final_copy(center) + [center_val_2] + final_copy(
        right_center) + [max_val] + final_copy(right_end)
# ###################################################################################

# Calling testing functions

# in_place_test()
multi_pivot()
# worst_case_test()
# factor_test()
# small_list_test(100)
# small_list_test(30)
