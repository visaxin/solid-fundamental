#!/usr/bin/env python
# encoding: utf-8

import sys

def _reverse(_str):
    result = ''
    _tmp = len(_str) - 1
    while _tmp >=0:
        result += _str[_tmp]
        _tmp -=1
    return result
def main():

    usage = 'Usage: python reverse.py  arg1 argv2 arg3'
    try:
        args = sys.argv[1:]
    except Exception as  e:
        print usage
        print e
        sys.exit(0)

    for argv in args:
        print _reverse(argv)



if __name__ == "__main__":
    main()
