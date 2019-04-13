#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: Listing_2_6_Using_a_session.py
#    Created:       <2019/04/11 18:10:27>
#    Last Modified: <2019/04/11 18:14:48>

import tensorflow as tf

x = tf.constant([[1., 2.]])
negMatrix = tf.negative(x)

with tf.Session() as sess:
    result = sess.run(negMatrix)
print(result)
