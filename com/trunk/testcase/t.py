# -*- coding: utf-8 -*-

import socket
import struct
from Tkinter import *  

def ipv4_text2int(ip):
    return struct.unpack('!i', socket.inet_aton(ip))[0]


def ipv4_int2text(n):
    return socket.inet_ntoa(struct.pack('!i', n))

if __name__ == '__main__':

#     root = Tk()                    # 创建窗口对象的背景色
#                                     # 创建两个列表
#     li     = ['C','python','php','html','SQL','java']
#     movie  = ['CSS','jQuery','Bootstrap']
#     listb  = Listbox(root)          #  创建两个列表组件
#     listb2 = Listbox(root)
#     for item in li:                 # 第一个小部件插入数据
#         listb.insert(0,item)
#     
#     for item in movie:              # 第二个小部件插入数据
#         listb2.insert(0,item)
#     
#     listb.pack()                    # 将小部件放置到主窗口中
#     listb2.pack()
#     root.mainloop()                 # 进入消息循环

    print ipv4_text2int("224.0.0.18")
    print ipv4_int2text(134250501)
    pass