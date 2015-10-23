#!/usr/bin/env python
# encoding: utf-8

from threading import Thread,Lock,Condition
import random
queue = []

condition = Condition()
class Producer(Thread):
    def run(self):
        global queue
        nums = random(5)
        while True:
            condition.acquire()
            num = random.choice(nums)
            queue.append(num)
            condition.notify()
            condition.release()

class Consumer(Thread):
    def run(self):
        global queue
        while True:
            if not queue:
                condition.wait()
            queue.pop()
            condition.release()
