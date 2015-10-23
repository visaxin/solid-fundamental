#!/usr/bin/env python
# encoding: utf-8
#a decorator to log with paramters
def log(log_format):
    def fn(function):
        def warpper(*args,**kwargs):

            print "[%s] %s...loging.."%(log_format,function.__name__)
            return function(*args,**kwargs)
        return warpper
    return fn


