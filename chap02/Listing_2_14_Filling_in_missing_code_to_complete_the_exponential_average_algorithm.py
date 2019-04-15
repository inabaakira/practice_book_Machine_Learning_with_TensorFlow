#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: Listing_2_14_Filling_in_missing_code_to_complete_the_exponential_average_algorithm.py
#    Created:       <2019/04/15 20:51:35>
#    Last Modified: <2019/04/15 20:55:13>

import tensorflow as tf
import numpy as np

raw_data = np.random.normal(10, 1, 100)

alpha = tf.constant(0.05)
curr_value = tf.placeholder(tf.float32)
prev_avg = tf.Variable(0.)
update_avg = alpha * curr_value + (1 - alpha) * prev_avg

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for i in range(len(raw_data)):
        curr_avg = sess.run(update_avg, feed_dict={curr_value: raw_data[i]})
        sess.run(tf.assign(prev_avg, curr_avg))
        print(raw_data[i], curr_avg)
