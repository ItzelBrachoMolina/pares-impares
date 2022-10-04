
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    
    
    if (n%2!=0):
        print("Weird")
    else:
        if(n==range(2,5)):
            print("not weird")
        else:
            print("weird")
             
