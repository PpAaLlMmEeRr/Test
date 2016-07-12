# -*- coding: utf-8 -*-
'''
Created on 2016��7��10��

@author: palmer
'''
from com.trunk.exception.Exceptions import ElementVisibleTimeout
# class ErrorWithArgs(Exception):
#     def __init__(self, *args):
#         # *args is used to get a list of the parameters passed in
#         self.args = [a for a in args]



if __name__ == '__main__':
    try:
        raise ElementVisibleTimeout(1, "text", "some more text")
    except ElementVisibleTimeout as e:
        print "%d: %s - %s" % (e.args[0], e.args[1], e.args[2])