# -*- coding: utf-8 -*-
'''
Created on 2016年7月13日

@author: Palmer.Piao
'''

if __name__ == '__main__':
    a = lambda x:x['id']
#     print sorted({"1":{"id":3},"2":{"id":6}}, key=lambda x:x['id'])
    print sorted([{"id":1}, {"id": 9}, {"id":5}], key=lambda x:x["id"])
    pass