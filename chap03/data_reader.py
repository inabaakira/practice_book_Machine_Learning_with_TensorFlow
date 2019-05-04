#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: data_reader.py
#    Created:       <2019/04/27 03:52:47>
#    Last Modified: <2019/04/27 03:56:54>

import csv
import time

def read(filename, date_idx, date_parse, year, bucket = 7):

    days_in_year = 365

    freq = {}
    for period in range(0, int(days_in_year / bucket)):
        freq[period] = 0

    with open(filename, 'rb') as csvfile:
        csvreader = csv.reader(csvfile)
        csvreader.next()
        for row in csvreader:
            if row[date_idx] == '':
                continue
            t = time.strptime(row[date_idx], date_parse)
            if t.tm_year = year and t.tm_yday < (days_in_year - 1):
                freq[int(t.tm_day / bucket)] += 1

    return freq

freq = read('311.csv', 0, '%m/%d/%Y', 2014)
