#!/usr/bin/env python
# encoding: utf-8


class Singleton():
    pass


single = Singleton()

'''
很早之前在stackoverflow 就看过这个问题，python的单例没有意思。
原文：
I don't really see the need, as a module with functions (and not a class) would serve well as a singleton. All its variables would be bound to the module, which could not be instantiated repeatedly anyways.

If you do wish to use a class, there is no way of creating private classes or private constructors in python, so you can't protect against multiple instantiations, other than just via convention in use of your API. I would still just put methods in a module, and consider the module as the singleton.
'''
