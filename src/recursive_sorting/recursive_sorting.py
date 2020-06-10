# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):

    elements = len(arrA) + len(arrB)   ## print(elements) --> 8
    merged_arr = [0] * elements   ## print('merged_arr', merged_arr) --> [0,0,0,0,0,0,0,0]
    # Your code here
    index_a = 0
    index_b = 0 
    print('arrA[index_a]', arrA[index_a])
    print('arrB[index_b]', arrB[index_b])
        # [2,66] [32,54]
    for i in range(elements):
        # print(i)
        if index_a  >= len(arrA):
            merged_arr[i] = arrB[index_b]
            index_b +=1
        elif index_b >= len(arrB):
            merged_arr[i] = arrA[index_a]
            index_a +=1
        # if A smaller put in list and iterate 
        elif  arrA[index_a] < arrB[index_b]:
            merged_arr[i] = arrA[index_a]
            index_a +=1
        else:
        # if B is smaller put in  lits and iterate 
            # arrA[index_a] > arrB[index_b]:
            merged_arr[i] = arrB[index_b]
            index_b +=1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:  # Base case
        return arr
    else:
        middle = len(arr) // 2
        left_side = merge_sort(arr[:middle]) #take everything on the left not including the middle
        right_side = merge_sort(arr[middle:]) #take everything on the right including middle
    return merge(left_side, right_side)

tester = [66,2,32,54,7,26,5,9]
# tester = [1,5,8,4,2,9,6,0,3,7]
print(merge_sort(tester))
# implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # Your code here
    new_start = mid + 1
    if (arr[mid] <= arr[new_start]):
        return
    while start <= mid and new_start <= end:
        if (arr[start]  <= arr[new_start]):
            start += 1
        else:
            value = arr[new_start]
            index = new_start

            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            
            arr[start] = value
            start += 1
            mid += 1
            new_start += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if len(arr) <= 1:
        return arr
    if l >= r:
        return arr
    middle = l + (r - l) // 2

    merge_sort_in_place(arr, l, middle)
    merge_sort_in_place(arr, middle + 1, r)
    merge_in_place(arr, l, middle, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr





#  class notes and other code {{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}

def partition(arr):
    left = []
    right = []
    pivot = arr[0]

    for i in arr[1:]:
        if i > pivot :
           right.append(i)
        else:
            left.append(i)
    return left, pivot, right

def quick_sort(arr):
    if len(arr) == 0:
        return arr

    left, pivot, right = partition(arr)
    return quick_sort(left) + pivot + quick_sort(right)

