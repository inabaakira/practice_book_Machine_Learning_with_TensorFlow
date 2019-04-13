#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: Listing_2_5_Using_the_negation_operator.py
#    Created:       <2019/04/10 16:52:46>
#    Last Modified: <2019/04/10 18:42:20>

import tensorflow as tf

x = tf.constant([[1, 2]])
negMatrix = tf.negative(x)
print(negMatrix)
with tf.Session() as sess:
    print("x = {}".format(x.eval()))
    print("negMatrix = {}".format(negMatrix.eval()))
