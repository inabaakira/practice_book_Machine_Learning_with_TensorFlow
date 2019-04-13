#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: Listing_2_8_Logging_a_session.py
#    Created:       <2019/04/11 21:06:35>
#    Last Modified: <2019/04/11 21:08:07>

import tensorflow as tf

x = tf.constant([[1., 2.]])
negMatrix = tf.negative(x)

with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
    result = sess.run(negMatrix)

print(result)
