# Example.py

from threading import _start_new_thread
from time import time
from copy import deepcopy
threadID = 1


def factorial(n):
    global threadID
    if n < 1:
        print("%s:%d" % ('Thread: ', threadID))
        threadID += 1
        return 1
    else:
        returnNumber = n*factorial(n-1)
        print(str(n) + '! = ' + str(returnNumber))
        return returnNumber


time1 = time()
_start_new_thread(factorial, (20,))
_start_new_thread(factorial, (15,))
time2 = time()
print('Time (4): ' + str(time2 - time1))


c = input("Wainting for threads\n")

