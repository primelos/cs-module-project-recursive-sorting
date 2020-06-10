# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):

    elements = len(arrA) + len(arrB)   ## print(elements) --> 8
    merged_arr = [0] * elements   ## print('merged_arr', merged_arr) --> [0,0,0,0,0,0,0,0]
    # Your code here
    index_a = 0
    index_b = 0 
    

    for i in range(elements):
        # print(i)
        # print(len(arrA))
        if index_a  >= len(arrA):
            merged_arr[i] = arrB[index_b]
            index_b +=1
        elif index_b >= len(arrB):
            merged_arr[i] = arrA[index_a]
            index_a +=1
        elif  arrA[index_a] < arrB[index_b]:
            merged_arr[i] = arrA[index_a]
            index_a +=1
        else:
            merged_arr[i] = arrB[index_b]
            index_b +=1
    return merged_arr

# arrA = [4, 2, 5, 1] 
# arrB = [6, 9, 8, 20]
# merge(arrA,arrB)
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        left_side = merge_sort(arr[:middle])
        right_side = merge_sort(arr[middle:])

    return merge(left_side, right_side)

tester = [66,2,32,54,7,26,9]
# tester = [1,5,8,4,2,9,6,0,3,7]
print(merge_sort(tester))
# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


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

