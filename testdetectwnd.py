# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:11:50 2023

@author: spark
"""

# from detectwnd import MyTimmer
# import time

# T=MyTimmer(0.1)
# T.start_count()
# while 1:
#     T.countUP()
#     time.sleep(1)
#     if T.isT():
#         print("done")
    
from detectwnd2 import DetectWnd
import time
bili=DetectWnd()

while 1:
    print('found hwnd')
    print(bili.get_hWnd_hand())
    # time.sleep(5)
    idx=0
    for i in bili.antiTimer:
        bili.mesg(idx)
        idx=idx+1
    bili.anticount()
    bili.forbid()
    time.sleep(5)