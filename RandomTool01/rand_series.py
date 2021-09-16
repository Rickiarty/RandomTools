#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    *                       *
    * coded by Rei-chi Lin  *
    *                       *
"""

import random
from time import time, ctime # import time for seeds for randomness
import sys

class RandomSeries:
    _list = []
    #_s_range = 0
    #_e_range = 1

    def __init__(self, range_start, range_end):
        self._list = [num for num in range(range_start, range_end)] # initialize a list with 'list comprehension' in Python
        #self._s_range = start_range
        #self._e_range = end_range

    @property
    def series(self):
        return self._list

    def rand_n_times(self, n):
        with open('priority_series.txt', 'w') as file:
            t = time()
            curr_dt = ctime(t)
            file.write(curr_dt + "\n")
            print(curr_dt)
            r_seed = int(t * 1000)
            random.seed(r_seed)
            length = len(self._list)
            for _ in range(n):
                index_a = random.randrange(0, length)
                index_b = random.randrange(0, length)
                # swap
                temp = self._list[index_a]
                self._list[index_a] = self._list[index_b]
                self._list[index_b] = temp
            file.write(str(self._list) + "\n")
            print(self._list)

def main():
    rand_obj = RandomSeries(int(sys.argv[1]), int(sys.argv[2]))
    rand_obj.rand_n_times(int(sys.argv[3]))
    #print(rand_obj.series)

if __name__ == '__main__':
    main()

