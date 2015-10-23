#!/usr/bin/env python
# encoding: utf-8

LENGTH = 10

class LRU(object):
    def __init__(self):
        self._lru_cache = []

    def put(self,item):
        '''
        if the current cache length is less than LENGTH
            then put directly
        else
            check if the new data is in cache
            if yes
                remove the origin item
                then update list header to item
            else
                then pop the last element in list
                put new item in header
        '''
        if len(self._lru_cache) <LENGTH:
                self._lru_cache.append(item)
        else:
            if item in self._lru_cache:
                self._lru_cache.remove(item)
                self._lru_cache.insert(0,item)

            else:
                self._lru_cache.pop()
                self._lru_cache.append(item)

    def clear(self):
        self._lru_cache = []

if __name__ == "__main__":
    s = LRU()


'''
LRU 一般作为cache的算法
还有是操作系统的页面置换算法，这个不熟悉。
'''
