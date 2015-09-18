

def iterativeBinarySearch(items, target):

    start = 0;
    last = len(items) - 1

    while start <= last:
        middle = (last - start) / 2
        if items[middle] == target:
            return True
        elif target < items[middle]:
            middle = last - 1
        else:
            middle = start + 1
