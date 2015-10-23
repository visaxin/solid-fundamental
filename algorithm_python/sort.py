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
# def insertion_sort_rec(seq, i = None):
# if i == None: i = len(seq) -1
# if i == 0: return i
# insertion_sort_rec(seq, i-1)
# j = i
# while j > 0 and seq[j-i] > seq[j]:
# seq[j-1], seq[j] = seq[j], seq[j-1]
# j -= 1
# return seq
# def test_insertion_sort():
# seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 6, 2, 5, 4, 1, 5, 3]
# assert(insertion_sort(seq) == sorted(seq))
# assert(insertion_sort_rec(seq) == sorted(seq))
# print(’Tests passed!’)
# if __name__ == ’__main__’:
# test_insertion_sort()
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
