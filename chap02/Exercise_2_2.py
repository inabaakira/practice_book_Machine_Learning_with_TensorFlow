#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: Exercise_2_2.py
#    Created:       <2019/04/10 21:16:46>
#    Last Modified: <2019/04/11 09:41:44>

import tensorflow as tf
from math import pi

mean = 0.0
sigma = 1.0

x = tf.placeholder(tf.float32)
y = (tf.exp(tf.negative(tf.pow(x - mean, 2.0) /
                      2.0 * tf.pow(sigma, 2.0))) *
     (1.0 / (sigma * tf.sqrt(2.0 * pi))))

with tf.Session() as sess:
    out = sess.run(y, feed_dict={x: 0.0})

print("value of normal distribution at 0.0: {}".format(out))
