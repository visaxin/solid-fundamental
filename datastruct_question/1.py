#!/usr/bin/env python
# encoding: utf-8

'''

define a stack structure.
implement a min function to get min in the stack
request: time O(1) pop push and min
'''


'''
solution: define a min data structure to maintain status
'''
class MinInStack():
    def __init__(self):
        self.min_in_stack = []
        self.top = []



class MyStack():
    def __init__(self,minStack):
        self.stack = []
        self.min_stack = minStack
    def pop(self):
        if len(self.stack) == 0:
            print "The stack is empty. No pop!"
            return
        if self.stack[len(self.stack)-1] == self.min.top:
            self.min_stack.min_in_stack =

        self.stack.pop()
    def push(self,x):
        self.stack.append(x)
        if self.min_stack.min_in_stack == "":
            self.min_stack.min_in_stack = x
            self.min_stack.top = x
        else:
            if self.min_stack.min_in_stack > x:
                self.min_stack.min_in_stack = x
                self.min_stack.top = x


