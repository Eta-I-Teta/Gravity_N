from engine.classes import *
from engine.utilities import *
from collections import deque

if __name__ == "__main__":
    #argparse
    

    #demo
    pass
l = deque(maxlen=5)
for i in range(10):
    l.append([i, i])
for i in l:
    print(i)