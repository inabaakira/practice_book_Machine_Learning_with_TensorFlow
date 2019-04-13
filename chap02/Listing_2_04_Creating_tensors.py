#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: Listing_2_4_Creating_tensors.py
#    Created:       <2019/04/10 13:58:25>
#    Last Modified: <2019/04/10 15:18:14>

import tensorflow as tf

m1 = tf.constant([[1., 2.]])

m2 = tf.constant([[1],
                  [2]])

m3 = tf.constant([ [[1, 2],
                    [3, 4],
                    [5, 6]],
                   [[7, 8],
                    [9, 10],
                    [11, 12]] ])

print(m1)
print(m2)
print(m3)


