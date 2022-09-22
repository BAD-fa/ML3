# # Python program for implementation of MergeSort
# def mergeSort(arr):
#     if len(arr) > 1:
#
#         # Finding the mid of the array
#         mid = len(arr) // 2
#
#         # Dividing the array elements
#         L = arr[:mid]
#
#         # into 2 halves
#         R = arr[mid:]
#
#         # Sorting the first half
#         mergeSort(L)
#
#         # Sorting the second half
#         mergeSort(R)
#
#         i = j = k = 0
#
#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i] <= R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#
#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
#
#
# # Code to print the list
#
#
# def printList(arr):
#     for i in range(len(arr)):
#         print(arr[i], end=" ")
#     print()
#
#
# # Driver Code
# if __name__ == '__main__':
#     arr = [12, 11, 13, 5, 6, 7]
#     print("Given array is", end="\n")
#     printList(arr)
#     mergeSort(arr)
#     print("Sorted array is: ", end="\n")
#     printList(arr)

# This code is contributed by Mayank Khanna


# ----------- another merge sort ---------

# import math
#
#
# def merge_sort(arr: list):
#     if len(arr) == 1:
#         return arr[0]
#
#     new_arr = []
#
#     for i in range(math.ceil(len(arr) / 2)):
#         try:
#             t = sorter(arr[2 * i], arr[(2 * i) + 1])
#         except IndexError:
#             t = sorter(arr[2 * i], [])
#         new_arr.append(t)
#
#     return merge_sort(new_arr)
#
#
# def sorter(a1, a2):
#     i = 0
#     j = 0
#     temp = []
#
#     while i < len(a1) and j < len(a2):
#         if a1[i] >= a2[j]:
#             temp.append(a2[j])
#             j += 1
#         else:
#             temp.append(a1[i])
#             i += 1
#
#     temp.extend(a1[i:])
#     temp += a2[j:]
#
#     return temp
#
#
# def divider(a):
#     return [int(a)]
#
#
# num_list = [int(i) for i in input().split(' ')]
# cut_num_list = list(map(divider, num_list))
#
# print("input", num_list)
# print("unsorted", cut_num_list)
# print("sorted", merge_sort(cut_num_list))
