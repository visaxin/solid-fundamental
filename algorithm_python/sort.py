#encoding=utf-8
#time: O(n) best
#O(n*n) worest
def insertion_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
    return seq
seq = [2,5,6,7,1,3,4,5,6,1000]

from collections import defaultdict
def count_sort_dic(seq):
    b, c = [], defaultdict(list)

    for x in seq:
        c[x].append(x)
    print c
    for k in range(min(c), max(c)+1):
        b.extend(c[k])
    return b

#print count_sort_dic(sq)

def merge_2n(left,right):
    if not left or not right:
        return left or right
    result = []

    while left and right:
        result.append(left.pop()  if left[-1] <= right[-1] else right.pop())
    while left:
        result.append(left.pop())
    while right:
        result.append(right.pop())
    result.reverse()

    return (left or right) + result
# def merge_n(left,right):
#     if not left or not right:
#         return left or right
#     result = []
#
#     l, r = 0, 0
#
#     while l < len(left) and r < len(right):
#         if left[l] < right[l]:
#             result.append(left[l])
#             l += 1
#         else:
#             result.append(right[r])
#             r += 1
#     if l < len(left) -1 :
#         reuslt+=left[l:]
#     elif r<len(right)-1:
#         result +=right[r:]
#     return result
def merge_sort(seq):
    if len(seq) < 2 : return seq
    mid = len(seq) // 2
    left, right = None, None
    if seq[:mid]:
        left = merge_sort(seq[:mid])
    if seq[mid:]:
        right = merge_sort(seq[mid:])

    return merge_n(left,right)


def quick_sort(seq = [56,34,58,26,79,52,64,37,28,84,57]):
    if len(seq) <=1:
        return seq
    else:
        return quick_sort([x for x in seq[1:] if x<seq[0]]) + [seq[0]] + quick_sort(x for x in seq[1:] if x> seq[0])

def quick_sort2(items):
    if len(items) < 2:
        return items
    else:
        return quick_sort2(x for x in items[1:] if x<seq[0])+\
                [items[0]] + quick_sort2(x for x in items[1:] if x>items[0])

#The best quick sort python code I ever seen

def best_sort(source = [2,3,5,1,6,8,100,34,54]):
    less = []
    eq = []
    greater = []
    if len(source) > 1:
        pivot = source[0]
        for x in source:
            if x > pivot:
                greater.append(x)
            if x == pivot:
                eq.append(x)
            if x < pivot:
                less.append(x)
        return best_sort(less) + pivot + best_sort(greater)
    else:
        return source
