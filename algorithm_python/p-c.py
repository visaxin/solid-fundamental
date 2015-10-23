#!/usr/bin/env python
# encoding: utf-8


from Queue import Queue
import random
import time
from threading import Thread
queue= Queue(10)

class Producer(Thread):
    def run(self):
        nums = range(5)
        global queue
        while(True):
            num = random.choice(nums)
            queue.put(num)
            print "Produced:",num
            time.sleep(random.random())

class Consumer(Thread):
    def run(self):
        global queue
        while(True):
            num = queue.get()
            queue.task_done()
            print "Consumed",num
            time.sleep(random.random)
