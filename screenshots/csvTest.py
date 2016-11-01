#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

s = "dataset_test.csv"
with open(s, 'rb') as f:
    reader = csv.reader(f)
    your_list = list(reader)


print ("The total array length {}".format(len(your_list)))
print ("Each Array has size {}".format(len(your_list[0])))


print (your_list[0])
"""
field need to be added:

"""
