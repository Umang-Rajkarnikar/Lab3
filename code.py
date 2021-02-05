import sorts.py

################################################################################################################

# IN-PLACE

def in_place_test():
    x_axis = []
    pivots = []
    for i in range(100, 10001, 100):
        pivots.append(create_random_list(i))
        x_axis.append(i)

    # Setup
    y_axis = []
    y_axis_inplace = []

    for i in pivots:
        x = i.copy()
        start = timeit.default_timer()
        my_quicksort(x)
        end = timeit.default_timer()
        y_axis.append(end - start)


    for i in pivots:
        x = i.copy()
        start = timeit.default_timer()
        quicksort_inplace(x)
        end = timeit.default_timer()
        y_axis_inplace.append(end - start)

    plt.scatter(x_axis, y_axis, label = "Quicksort")
    plt.scatter(x_axis, y_axis_inplace, label = "In-Place Quicksort")
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
    x.sort(reverse = True)
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
         factor_list.append(create_near_sorted_list(1000, i/100))
         x_axis_factor.append(i/100)

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

    plt.scatter(x_axis_factor, y_quick, label = "Quick sort - Quad pivot")
    plt.scatter(x_axis_factor, y_bubble, label = "Bubble sort")
    plt.scatter(x_axis_factor, y_selection, label = "Selection sort")
    plt.scatter(x_axis_factor, y_insertion, label = "Insertion sort")
    plt.title("Quicksort vs. Elementary Sorts vs. Near-Sorted Factor")
    plt.xlabel("Near-Sorted Factor")
    plt.ylabel("Runtime")
    plt.legend()
    plt.show()

###############################################################################################################

# SMALL LISTS

def small_list_test():
    factor_list = []
    x_axis_factor = []
    y_quick = []
    y_bubble = []
    y_insertion = []
    y_selection = []

    for i in range(5, 100, 2):
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

    plt.scatter(x_axis_factor, y_quick, label = "Quick sort - Quad pivot")
    plt.scatter(x_axis_factor, y_bubble, label = "Bubble sort")
    plt.scatter(x_axis_factor, y_selection, label = "Selection sort")
    plt.scatter(x_axis_factor, y_insertion, label = "Insertion sort")
    plt.title("Quicksort vs. Elementary Sorts vs. List Size (n)")
    plt.xlabel("List Size (n)")
    plt.ylabel("Runtime")
    plt.legend()
    plt.show()

####################################################################################

# Calling testing functions

in_place_test()
# multi_pivot()
# worst_case_test()
# factor_test()
# small_list_test()