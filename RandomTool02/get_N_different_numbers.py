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

def get_N_diff_nums(N, start, end):
    # a function/method to generate a list of N non-duplicate random numbers between 'start' and 'end', NOT including 'end' itself. 
    list = [] # an empty list
    t = time() # to get current time as a seed for randomness
    curr_dt_str = ctime(t) # to fit current time to a string in standard format of date-time 
    # make it a seed for randomness 
    r_seed = int(t * 1000)
    random.seed(r_seed)
    while True: # infinite loop
        num = random.randrange(start, end) # to get a random number between 'start' and 'end', NOT including 'end' itself. 
        if not num in list:
            list.append(num) # to append last to the list 
        if len(list) >= N:
            break # to break the closest loop
    return curr_dt_str, list

if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
        s = int(sys.argv[2])
        e = int(sys.argv[3])
        curr_dt_str, list_of_nums = get_N_diff_nums(n, s, e+1) # to get a list of non-duplicate random numbers between 's' and 'e', including 'e' itself. 
        with open('list_of_names.txt', 'w') as file:
            file.write(curr_dt_str + "\n")
            print(curr_dt_str)
            file.write('list = {}\n'.format(str(list_of_nums)))
            print('list = {}'.format(str(list_of_nums)))
    except Exception as ex:
        print(str(ex))
