

def iterativeBinarySearch(items, target):

    start = 0;
    last = len(items) - 1

    while start <= last:
        middle = (last - start) / 2
        if items[middle] == target:
            return True
        elif target < items[middle]:
            last = middle - 1
        else:
            first = middle + 1


def binarySearch(items,target):
    lower = 0
    upper = len(items)-1

    while(lower < upper):
        middle = (upper - lower) /2

        if items[middle] == target:
            return middle
        else if items[middle] > target:
            upper = middle-1
        else:
            lower = middler+1
